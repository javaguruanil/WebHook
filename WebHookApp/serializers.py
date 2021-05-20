from flask_restplus import fields
#from apps import app
import apps

training_record = apps.app.model('Training record', {
    #'_id': fields.Integer(readOnly=True, description='The unique identifier of a training record'),
    'borough': fields.String(required=True, description='Borough'),
    'job_type': fields.String(required=True, description='Job Type/Sector'),
    'training_option': fields.String(description='Training Options Available'),
    'find_out_more': fields.String(description='To find out more')
    })

training_record_response = apps.app.clone('Training record response', training_record, {
    '_id': fields.String(readOnly=True, description='The unique identifier of a training record')
    })
