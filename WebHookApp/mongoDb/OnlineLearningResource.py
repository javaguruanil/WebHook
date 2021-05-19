from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson


def getOnlineLearnResources(data):
    return {
            WebHookConstants.SKILL_TYPES.value : data[WebHookConstants.SKILL_TYPES.value],
            WebHookConstants.CORRESPONDING_ONLINE_LINKS.value : data[WebHookConstants.CORRESPONDING_ONLINE_LINKS.value],
            WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveOnlineLearnResources(data):
    result = WebHookConstants.ONLINE_LEARN_RESOURCES_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .ONLINE_LEARN_RESOURCES \
             .insert_one(getOnlineLearnResources(data))
        mongo.close()
        result = WebHookConstants.ONLINE_LEARN_RESOURCES_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the OnlineLearnResources insertion :: ", ex)
    return result

def fetchOnlineLearnResources(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ONLINE_LEARN_RESOURCES \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
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
                         WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ONLINE_LEARN_RESOURCES \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the OnlineLearnResources deleting :: ", ex)
    return getDeleteJson(result)


def updateOnlineLearnResources(data):
    result = None
    queryFilter = {WebHookConstants.ID.value:
                   ObjectId(data[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ONLINE_LEARN_RESOURCES \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the OnlineLearnResources updating :: ", ex)
    return getUpdateJson(result, WebHookConstants.NO_RECORDS_UPDATED.value)
