from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson


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
    return result

def fetchVacancies(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .VACANCIES \
                      .find_one(WebHookUtil.appendSoftDeleteNo(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Vacancies fetching :: ", ex)
    return getJson(result)

def deleteVacancies(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                       'update_date' : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .VACANCIES \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Vacancies deleting :: ", ex)
    return getDeleteJson(result)
