from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson


def getNonAccreditedJson(data):
    return {
            WebHookConstants.BOROUGH.value : data[WebHookConstants.BOROUGH.value],
            WebHookConstants.SUBJECT.value : data[WebHookConstants.SUBJECT.value],
            WebHookConstants.POSSIBLE_OPTIONS.value : data[WebHookConstants.POSSIBLE_OPTIONS.value],
            WebHookConstants.WHERE_TO_FIND_MORE.value : data[WebHookConstants.WHERE_TO_FIND_MORE.value],
            WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveNonAccredited(data):
    result = WebHookConstants.NON_ACCREDITED_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .NON_ACCREDITED \
             .insert_one(getNonAccreditedJson(data))
        mongo.close()
        result = WebHookConstants.NON_ACCREDITED_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the NonAccredited insertion :: ", ex)
    return result

def fetchNonAccredited(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .NON_ACCREDITED \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the NonAccredited fetching :: ", ex)
    return getJson(result)

def deleteNonAccredited(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                         WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .NON_ACCREDITED \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the NonAccredited deleting :: ", ex)
    return getDeleteJson(result)

def updateNonAccredited(data):
    result = None
    queryFilter = {WebHookConstants.ID.value:
                       ObjectId(data[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .NON_ACCREDITED \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the NonAccredited updating :: ", ex)
    return getUpdateJson(result, WebHookConstants.NO_RECORDS_UPDATED.value)