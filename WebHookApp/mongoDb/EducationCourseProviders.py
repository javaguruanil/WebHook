from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson


def getEduCourseProvidersJson(data):
    return {
            WebHookConstants.COURSES.value : data[WebHookConstants.COURSES.value],
            WebHookConstants.PROVIDER_ADDRESS.value : data[WebHookConstants.PROVIDER_ADDRESS.value],
            WebHookConstants.SCHEDULE_COST.value : data[WebHookConstants.SCHEDULE_COST.value],
            WebHookConstants.FURTHER_INFO.value : data[WebHookConstants.FURTHER_INFO.value],
            WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
            WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveEducationCourseProviders(data):
    result = WebHookConstants.EDU_COURSE_PROVIDERS_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV\
             .EDU_COURSE_PROVIDERS\
             .insert_one(getEduCourseProvidersJson(data))
        mongo.close()
        result = WebHookConstants.EDU_COURSE_PROVIDERS_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the EducationCourseProviders insertion :: ", ex)
    return result

def fetchEducationCourseProviders(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .EDU_COURSE_PROVIDERS \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the EducationCourseProviders fetching :: ", ex)
    return getJson(result)

def deleteEducationCourseProviders(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                         WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .EDU_COURSE_PROVIDERS \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the EducationCourseProviders deleting :: ", ex)
    return getDeleteJson(result)

def updateEducationCourseProviders(data):
    result = None
    queryFilter = {WebHookConstants.ID.value:
                    ObjectId(data[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .EDU_COURSE_PROVIDERS \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the EducationCourseProviders updating :: ", ex)
    return getUpdateJson(result, WebHookConstants.NO_RECORDS_UPDATED.value)
