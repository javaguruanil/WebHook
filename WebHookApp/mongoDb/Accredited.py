from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson, getDeleteMessage, \
    getUpdateMessage
from WebHookApp.response.AccreditedFetch import AccreditedFetch


def getAccreditedJson(data):
    return {
            WebHookConstants.BOROUGH.value : data[WebHookConstants.BOROUGH.value],
            WebHookConstants.SUBJECT.value : data[WebHookConstants.SUBJECT.value],
            WebHookConstants.POSSIBLE_OPTIONS.value : data[WebHookConstants.POSSIBLE_OPTIONS.value],
            WebHookConstants.WHERE_TO_FIND_MORE.value : data[WebHookConstants.WHERE_TO_FIND_MORE.value],
            WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveAccredited(data):
    result = WebHookConstants.ACCREDITED_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        result = mongo.webHook_DEV \
                      .ACCREDITED \
                      .insert_one(getAccreditedJson(data))
        mongo.close()
        result = str(result.inserted_id)+WebHookConstants.HYPHEN.value+WebHookConstants.ACCREDITED_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the Accredited insertion :: ", ex)
    return result

def fetchAccredited(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ACCREDITED \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Accredited fetching :: ", ex)
    if result is None:
        return WebHookConstants.NO_RECORDS_FOUND.value
    else:
        resp = getJson(result)
        resp[WebHookConstants.ID.value] = resp[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value]
        return AccreditedFetch(**resp)

def deleteAccredited(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                        WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ACCREDITED \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Accredited deleting :: ", ex)
    return getDeleteMessage(result)

def updateAccredited(data):
    result = None
    queryFilter = {WebHookConstants.ID.value:ObjectId(data[WebHookConstants.ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .ACCREDITED \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Accredited updating :: ", ex)
    return getUpdateMessage(result, WebHookConstants.NO_RECORDS_UPDATED.value)