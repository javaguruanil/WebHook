from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson


def getOnlineLearnResources(data):
    return {
        'skill_types' : data['skill_types'],
        'corresponding_online_links' : data['corresponding_online_links'],
        'create_date' : getCurrentDateTime(),
        'update_date' : getCurrentDateTime(),
        'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveOnlineLearnResources(data):
    result = "OnlineLearnResources data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .ONLINE_LEARN_RESOURCES \
             .insert_one(getOnlineLearnResources(data))
        mongo.close()
        result = "OnlineLearnResources Created"
    except Exception as ex:
        print("Error occurred during the OnlineLearnResources insertion :: ", ex)
    return result

def fetchOnlineLearnResources(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ONLINE_LEARN_RESOURCES \
                      .find_one(WebHookUtil.appendSoftDeleteNo(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the OnlineLearnResources fetching :: ", ex)
    return getJson(result)

def deleteOnlineLearnResources(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                       'update_date' : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ONLINE_LEARN_RESOURCES \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the OnlineLearnResources deleting :: ", ex)
    return getDeleteJson(result)
