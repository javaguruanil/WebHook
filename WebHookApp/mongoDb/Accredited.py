from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson


def getAccreditedJson(data):
    return {
        'borough' : data['borough'],
        'subject' : data['subject'],
        'possible_options' : data['possible_options'],
        'where_to_find_more' : data['where_to_find_more'],
        'create_date' : getCurrentDateTime(),
        'update_date' : getCurrentDateTime(),
        'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveAccredited(data):
    result = "Accredited data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .ACCREDITED \
             .insert_one(getAccreditedJson(data))
        mongo.close()
        result = "Accredited Created"
    except Exception as ex:
        print("Error occurred during the Accredited insertion :: ", ex)
    return result

def fetchAccredited(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ACCREDITED \
                      .find_one(WebHookUtil.appendSoftDeleteNo(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Accredited fetching :: ", ex)
    return getJson(result)