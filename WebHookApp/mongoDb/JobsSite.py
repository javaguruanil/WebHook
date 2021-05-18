from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime


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
    return result;
