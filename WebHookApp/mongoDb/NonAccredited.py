from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime


def getNonAccreditedJson(data):
    return {
        'borough' : data['borough'],
        'subject' : data['subject'],
        'possible_options' : data['possible_options'],
        'where_to_find_more' : data['where_to_find_more'],
        'create_date' : getCurrentDateTime(),
        'update_date' : getCurrentDateTime(),
        'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveNonAccredited(data):
    result = "NonAccredited data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .NON_ACCREDITED \
             .insert_one(getNonAccreditedJson(data))
        mongo.close()
        result = "NonAccredited Created"
    except Exception as ex:
        print("Error occurred during the NonAccredited insertion :: ", ex)
    return result;