from bson import ObjectId

from WebHookApp.mongoDb import WebHookUtil
from WebHookApp.mongoDb.MongoDBConnector import getConnection
from WebHookApp.mongoDb.WebHookConstants import WebHookConstants
from WebHookApp.mongoDb.WebHookUtil import getCurrentDateTime, getJson, getDeleteJson, getUpdateJson, getDeleteMessage, \
    getUpdateMessage
from WebHookApp.response.Covid19EmploymentPgmFetch import Covid19EmploymentPgmFetch


def getCovid19EmploymentPgmJson(data):
    return {
        WebHookConstants.SKILL_TYPES.value : data[WebHookConstants.SKILL_TYPES.value],
        WebHookConstants.CORRESPONDING_ONLINE_LINKS.value : data[WebHookConstants.CORRESPONDING_ONLINE_LINKS.value],
        WebHookConstants.CREATE_DATE.value : getCurrentDateTime(),
        WebHookConstants.UPDATE_DATE.value : getCurrentDateTime(),
        WebHookConstants.SOFT_DELETE.value : WebHookConstants.SOFT_DEL_FLAG_NO.value
    }

def saveCovid19EmploymentPgm(data):
    result = WebHookConstants.COVID19_EMP_PGM_DATA_NOT_CREATED.value
    try:
        mongo = getConnection()
        # TODO - Need to set configurations for DEV, QA, PERF, ACCEPTANCE envs
        result = mongo.webHook_DEV \
                      .COVID19_EMPLOYMENT_PRGM \
                      .insert_one(getCovid19EmploymentPgmJson(data))
        mongo.close()
        result =  str(result.inserted_id)+WebHookConstants.HYPHEN.value\
                  +WebHookConstants.COVID19_EMP_PGM_DATA_CREATED.value
    except Exception as ex:
        print("Error occurred during the Covid19EmploymentPgm insertion :: ", ex)
    return result

def fetchCovid19EmploymentPgm(data):
    result = None
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .COVID19_EMPLOYMENT_PRGM \
                      .find_one(WebHookUtil.appendSoftDeleteNoAndObjectId(data))
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Covid19EmploymentPgm fetching :: ", ex)
    if result is None:
        return WebHookConstants.NO_RECORDS_FOUND.value
    else:
        resp = getJson(result)
        resp[WebHookConstants.ID.value] = resp[WebHookConstants.ID.value][WebHookConstants.OBJECT_ID.value]
        return Covid19EmploymentPgmFetch(**resp)

def deleteCovid19EmploymentPgm(id):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(id)}
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value
                     :{WebHookConstants.SOFT_DELETE.value
                       :WebHookConstants.SOFT_DEL_FLAG_YES.value,
                        WebHookConstants.UPDATE_DATE.value : getCurrentDateTime()}}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .COVID19_EMPLOYMENT_PRGM \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Covid19EmploymentPgm deleting :: ", ex)
    return getDeleteMessage(result)

def updateCovid19EmploymentPgm(data):
    result = None
    queryFilter = {WebHookConstants.ID.value: ObjectId(data[WebHookConstants.ID.value])}
    data[WebHookConstants.UPDATE_DATE.value] = getCurrentDateTime()
    del data[WebHookConstants.ID.value]
    updatingValue = {WebHookConstants.UPDATE_EXPRESSION.value: data}
    try:
        mongo = getConnection()
        result = mongo.webHook_DEV \
                      .COVID19_EMPLOYMENT_PRGM \
                      .update_one(queryFilter, updatingValue)
        mongo.close()
    except Exception as ex:
        print("Error occurred during the Covid19EmploymentPgm updating :: ", ex)
    return getUpdateMessage(result, WebHookConstants.NO_RECORDS_UPDATED.value)
