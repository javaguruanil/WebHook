from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime


def getVacanciesJson(data):
    return {
        'skill_type' : data['skill_type'],
        'career_options_for_skills' : data['career_options_for_skills'],
        'further_info' : data['further_info'],
        'create_date' : getCurrentDateTime(),
        'update_date' : getCurrentDateTime(),
        'soft_delete' : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveVacancies(data):
    result = "Vacancies data not inserted."
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        mongo.webHook_DEV \
             .VACANCIES \
             .insert_one(getVacanciesJson(data))
        mongo.close()
        result = "Vacancies Created"
    except Exception as ex:
        print("Error occurred during the Vacancies insertion :: ", ex)
    return result;