from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson


def getEduCourseProvidersJson(data):
    return {
        'courses' : data['courses'],
        'provider_address' : data['provider_address'],
        'schedule_cost' : data['schedule_cost'],
        'further_info' : data['further_info'],
        'create_date' : getCurrentDateTime(),
        'update_date' : getCurrentDateTime(),
        'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveEducationCourseProviders(data):
    result = "EducationCourseProviders data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV\
             .EDU_COURSE_PROVIDERS\
             .insert_one(getEduCourseProvidersJson(data))
        mongo.close()
        result = "EducationCourseProviders Created"
    except Exception as ex:
        print("Error occurred during the EducationCourseProviders insertion :: ", ex)
    return result

def fetchEducationCourseProviders(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .EDU_COURSE_PROVIDERS \
                      .find_one(WebHookUtil.appendSoftDeleteNo(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the EducationCourseProviders fetching :: ", ex)
    return getJson(result)