from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime


def getCovid19EmploymentPgmJson(data):
    return {
        'skill_types' : data['skill_types'],
        'corresponding_online_links' : data['corresponding_online_links'],
        'create_date' : getCurrentDateTime(),
        'update_date' : getCurrentDateTime(),
        'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveCovid19EmploymentPgm(data):
    result = "Covid19EmploymentPgm data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .COVID19_EMPLOYMENT_PRGM \
             .insert_one(getCovid19EmploymentPgmJson(data))
        mongo.close()
        result = "Covid19EmploymentPgm Created"
    except Exception as ex:
        print("Error occurred during the Covid19EmploymentPgm insertion :: ", ex)
    return result;