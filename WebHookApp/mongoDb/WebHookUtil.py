import json
from datetime import datetime

from bson import json_util

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


def appendSoftDeleteNo(data):
    """
    This function appends json attribute soft_delete:no
    :param data:
    :return: json string
    """
    data[WebHookConstants.SOFT_DELETE.value] = WebHookConstants.SOFT_DEL_FLAG_NO.value
    return data
