import json
from datetime import datetime

from bson import json_util, ObjectId

from WebHookApp.mongoDb.WebHookConstants import WebHookConstants


def getCurrentDateTime():
    """
    This function returns current day - date and time
    :return: str
    """
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def getJson(data):
    """
    This function serializes ObjectId which is non-serialized.
    :param data: json string
    """
    if data is None:
        return {WebHookConstants.MESSAGE.value: WebHookConstants.NO_RECORDS_FOUND.value}
    else:
        return json.loads(json_util.dumps(data))


def appendSoftDeleteNoAndObjectId(data):
    """
    This function appends json attribute soft_delete:no
    :param data:
    :return: json string
    """
    data = appendObjectId(data)
    data[WebHookConstants.SOFT_DELETE.value] = WebHookConstants.SOFT_DEL_FLAG_NO.value
    return data

def appendObjectId(data):
    if WebHookConstants.ID.value in data:
        data[WebHookConstants.ID.value] = ObjectId(data[WebHookConstants.ID.value])
    return data

def getDeleteJson(data):
    if data is None:
        return {WebHookConstants.MESSAGE.value: WebHookConstants.NO_RECORDS_FOUND.value}
    else:
        return {WebHookConstants.MESSAGE.value: WebHookConstants.RECORD_DELETED.value}

def getUpdateJson(data, message):
    """
    This function serializes ObjectId which is non-serialized.
    :param message: string
    :param data: json string
    """
    if data is None or (data is not None and data.modified_count == 0):
        return {WebHookConstants.MESSAGE.value: message}
    else:
        return {WebHookConstants.MESSAGE.value: WebHookConstants.RECORDS_UPDATED.value}
