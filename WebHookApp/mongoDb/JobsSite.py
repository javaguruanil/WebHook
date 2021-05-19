from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson


#TODO - Need to move constants to enum.
def getJobsSiteJson(data):
    return {
             'job_category' : data['job_category'],
             'corresponding_job_site' : data['corresponding_job_site'],
             'create_date' : getCurrentDateTime(),
             'update_date' : getCurrentDateTime(),
             'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
           }

def saveJobsSite(data):
    result = "JobsSite data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV\
             .JOBS_SITE\
             .insert_one(getJobsSiteJson(data))
        mongo.close()
        result = "JobsSite Created"
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
    return getJson(result)


def deleteJobsSite(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                       'update_date' : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .JOBS_SITE \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the JobsSite deleting :: ", ex)
    return getDeleteJson(result)

def updateJobsSite(data):
    result = None
    queryFilter = {WebHookConstants.ID.value:
                   ObjectId(data[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value])}
    data['update_date'] = getCurrentDateTime()
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
    return getUpdateJson(result, WebHookConstants.NO_RECORDS_UPDATED.value)
