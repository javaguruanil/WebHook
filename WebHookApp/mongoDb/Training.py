from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson


def getTrainingJson(data):
    return {
        WebHookConstants.BOROUGH.value : data[WebHookConstants.BOROUGH.value],
        WebHookConstants.SECTOR_OR_JOB_TYPE.value : data[WebHookConstants.SECTOR_OR_JOB_TYPE.value],
        WebHookConstants.TRAINING_OPTION.value : data[WebHookConstants.TRAINING_OPTION.value],
        WebHookConstants.WHERE_TO_FIND_MORE.value : data[WebHookConstants.WHERE_TO_FIND_MORE.value],
        WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
        WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
        WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveTraining(data):
    result = WebHookConstants.TRAINING_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .TRAINING \
             .insert_one(getTrainingJson(data))
        mongo.close()
        result = WebHookConstants.TRAINING_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the Training insertion :: ", ex)
    return result

def fetchTraining(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .TRAINING \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Training fetching :: ", ex)
    return getJson(result)

def deleteTraining(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                         WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .TRAINING \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Training deleting :: ", ex)
    return getDeleteJson(result)

def updateTraining(data):
    result = None
    queryFilter = {WebHookConstants.ID.value:
                       ObjectId(data[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .TRAINING \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Training updating :: ", ex)
    return getUpdateJson(result, WebHookConstants.NO_RECORDS_UPDATED.value)