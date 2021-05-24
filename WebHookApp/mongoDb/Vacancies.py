from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson, getDeleteMessage, \
    getUpdateMessage
from WebHookApp.response.VacanciesFetch import VacanciesFetch


def getVacanciesJson(data):
    return {
        WebHookConstants.SKILL_TYPE.value : data[WebHookConstants.SKILL_TYPE.value],
        WebHookConstants.CAREER_OPTIONS_FOR_SKILLS.value : data[WebHookConstants.CAREER_OPTIONS_FOR_SKILLS.value],
        WebHookConstants.FURTHER_INFO.value : data[WebHookConstants.FURTHER_INFO.value],
        WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
        WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
        WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveVacancies(data):
    result = WebHookConstants.VACANCIES_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        result = mongo.webHook_DEV \
                      .VACANCIES \
                      .insert_one(getVacanciesJson(data))
        mongo.close()
        result = str(result.inserted_id)+WebHookConstants.HYPHEN.value\
                 +WebHookConstants.VACANCIES_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the Vacancies insertion :: ", ex)
    return result

def fetchVacancies(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .VACANCIES \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Vacancies fetching :: ", ex)
    if result is None:
        return WebHookConstants.NO_RECORDS_FOUND.value
    else:
        resp = getJson(result)
        resp[WebHookConstants.ID.value] = resp[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value]
        return VacanciesFetch(**resp)

def deleteVacancies(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                         WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .VACANCIES \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Vacancies deleting :: ", ex)
    return getDeleteMessage(result)

def updateVacancies(data):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(data[WebHookConstants.ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .VACANCIES \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Vacancies updating :: ", ex)
    return getUpdateMessage(result, WebHookConstants.NO_RECORDS_UPDATED.value)

