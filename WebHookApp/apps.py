from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
from lmiforall.apis import *
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import logging

flask_app = Flask(__name__)

flask_app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/webhook'
flask_app.config['RESTPLUS_MASK_SWAGGER'] = False
mongo = PyMongo(flask_app)

app = Api(app = flask_app, version='1.0', title='Webhook API',
          description='A simple API documentation of Webhook APIs')

logging.basicConfig(filename='webhook.log', level=logging.DEBUG, format=f'[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')

training_db = mongo.db.training

lmiforall_ns = app.namespace('lmiforall', description='Lmiforall APIs')
#@flask_app.route("/")
#def hello():
#    app.logger.debug("LOGS")
#    return "Hello World!"

@lmiforall_ns.route("/vacancies")
class VcanciesLmiforallAPI(Resource):
    @lmiforall_ns.doc(params={'keywords': {'description': 'Keyword to search for', 'type': 'string', 'required': True},
                              'location': {'description': 'Restrict search around a location or postcode. You may also use this as \'postcode\' for backwards compatibility.', 'type': 'text'},
                              'radius': {'description': 'Search radius around location (default: 50).', 'type': 'text'},
                              'limit': {'description': 'Limit results to this many entries. Default and maximum is 50.', 'type': 'text'}})
    def get(self):
        keywords = request.args.get('keywords', None)
        location = request.args.get('location', None)
        radius = request.args.get('radius', None)
        limit = request.args.get('limit', None)

        if keywords == None:
            return jsonify({"status":"error", "errorMessage": "Please provide a keyword to search for vacancies"})

        return jsonify(Vacancies.get_vacancies(keywords, location, radius, limit))

@lmiforall_ns.route("/courses")
class CourcesLmiforallAPI(Resource):
    @lmiforall_ns.doc(params={'subject': {'description': 'Course subject/title (text search).', 'type': 'string', 'required': True}, 
                              'postcode': {'postcode': 'Courses offered within a certain distance of this postcode.', 'type': 'string'}})
    def get(self):
        subject = request.args.get('subject', None)
        if subject == None:
            return jsonify({"status":"error", "errorMessage": "Please provide a subject to search for cources"})
        postcode = request.args.get('postcode', None)

        return jsonify(Courses.get_courses(subject, postcode))


from serializers import *

training_ns = app.namespace('training', description='Training available in different sectors APIs')

@training_ns.route("/")
class TrainingAPI(Resource):
    @lmiforall_ns.doc(params={'borough': {'description': 'Borough to search for training', 'type': 'string'}})
    @app.doc(description='Get a list of all the training available')
    @app.marshal_list_with(training_record_response, code=200, description='Get a list of all the training available')
    def get(self):
        borough = request.args.get('borough', None)
        if borough == None:
            trainings = training_db.find()
        else:
            trainings = training_db.find({'borough': borough.lower()})

        response = []
        for training in trainings:
            new_training = {}
            new_training["_id"] = str(training["_id"])
            new_training["borough"] = training["borough"]
            new_training["job_type"] = training["job_type"]
            new_training["training_option"] = training["training_option"]
            new_training["find_out_more"] = training["find_out_more"]
            response.append(new_training)

        return response

    @app.doc(description='Create a new training program')
    @app.response(201, 'Training successfully created.')
    @app.expect(training_record)
    def post(self):
        data = request.json
        record = {
            "borough": data.get("borough").lower(),
            "job_type": data.get("job_type", "").lower(),
            "training_option": data.get("training_option", "").lower(),
            "find_out_more": data.get("find_out_more", "")
        }
        training_db.insert_one(record)
        return None, 201

@training_ns.route("/<string:oid>")
class TraningRecordAPI(Resource):
    @app.doc(description='Get a particular training')
    @app.marshal_with(training_record_response, code=200, description='Get a particular training record')
    def get(self, oid):
        training = training_db.find_one({'_id': ObjectId(oid)})
        return training

    @app.doc(description='Delete a particular training')
    @app.response(204, 'Training successfully deleted.')
    def delete(self, oid):
        training_db.delete_one({'_id': ObjectId(oid)})
        return None, 204

    @app.doc(description='Update a particular training')
    @app.response(204, 'Training successfully updated.')
    @app.expect(training_record)
    def put(self, oid):
        training = request.json
        new_training = training_db.find_one({'_id': ObjectId(oid)})
        new_training["borough"] = training.get("borough", new_training["borough"]).lower()
        new_training["job_type"] = training.get("job_type", new_training["job_type"]).lower()
        new_training["training_option"] = training.get("training_option", new_training["training_option"]).lower()
        new_training["find_out_more"] = training.get("find_out_more", new_training["find_out_more"])
        training_db.save(new_training)
        return None, 200


if __name__ == "__main__":
    app.run()
