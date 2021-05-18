from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime


def getTrainingJson(data):
    return {
        'borough' : data['borough'],
        'sector_or_job_type' : data['sector_or_job_type'],
        'training_option' : data['training_option'],
        'where_to_find_more' : data['where_to_find_more'],
        'create_date' : getCurrentDateTime(),
        'update_date' : getCurrentDateTime(),
        'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveTraining(data):
    result = "Training data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .TRAINING \
             .insert_one(getTrainingJson(data))
        mongo.close()
        result = "Training Created"
    except Exception as ex:
        print("Error occurred during the Training insertion :: ", ex)
    return result;