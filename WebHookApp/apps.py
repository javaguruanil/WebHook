from flask import Flask, jsonify, request
from lmiforall.apis import *

import logging

app = Flask(__name__)

logging.basicConfig(filename='webhook.log', level=logging.DEBUG, format=f'[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')

@app.route("/")
def hello():
    app.logger.debug("LOGS")
    return "Hello World!"

@app.route("/vacancies")
def get_vacancies():
    keywords = request.args.get('keywords', None)
    location = request.args.get('location', None)
    radius = request.args.get('radius', None)
    limit = request.args.get('limit', None)

    if keywords == None:
        return jsonify({"status":"error", "errorMessage": "Please provide a keyword to search for vacancies"})

    return jsonify(Vacancies.get_vacancies(keywords, location, radius, limit))

@app.route("/courses")
def get_courses():
    subject = request.args.get('subject', None)
    if subject == None:
        return jsonify({"status":"error", "errorMessage": "Please provide a subject to search for cources"})
    postcode = request.args.get('postcode', None)

    return jsonify(Courses.get_courses(subject, postcode))

if __name__ == "__main__":
    app.run()
