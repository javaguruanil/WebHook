from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson, getDeleteMessage, \
    getUpdateMessage
from WebHookApp.response.JobsSiteFetch import JobsSiteFetch


def getJobsSiteJson(data):
    return {
            WebHookConstants.JOB_CATEGORY.value : data[WebHookConstants.JOB_CATEGORY.value],
            WebHookConstants.CORRESPONDING_JOB_SITE.value : data[WebHookConstants.CORRESPONDING_JOB_SITE.value],
            WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveJobsSite(data):
    result = WebHookConstants.JOBS_SITE_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        result = mongo.webHook_DEV\
                      .JOBS_SITE\
                      .insert_one(getJobsSiteJson(data))
        mongo.close()
        result = str(result.inserted_id)+WebHookConstants.HYPHEN.value+WebHookConstants.JOBS_SITE_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the JobsSite insertion :: ", ex)
    return result

def fetchJobsSite(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .JOBS_SITE \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the JobsSite fetching :: ", ex)
    if result is None:
        return WebHookConstants.NO_RECORDS_FOUND.value
    else:
        resp = getJson(result)
        resp[WebHookConstants.ID.value] = resp[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value]
        return JobsSiteFetch(**resp)


def deleteJobsSite(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                         WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .JOBS_SITE \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the JobsSite deleting :: ", ex)
    return getDeleteMessage(result)

def updateJobsSite(data):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(data[WebHookConstants.ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .JOBS_SITE \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the JobsSite updating :: ", ex)
    return getUpdateMessage(result, WebHookConstants.NO_RECORDS_UPDATED.value)
