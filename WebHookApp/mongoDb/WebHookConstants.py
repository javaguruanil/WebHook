from enum import Enum
class WebHookConstants(Enum):
    SOFT_DEL_FLAG_NO = "No"
    SOFT_DEL_FLAG_YES = "Yes"
    MESSAGE = "msg"
    NO_RECORDS_FOUND = "No records found for given data."
    SOFT_DELETE = "soft_delete"
    ID = "_id"
    UPDATE_EXPRESSION = "$set"
    RECORD_DELETED = "Record is deleted successfully."
    NO_RECORDS_UPDATED = "No records are updated, please check !!!!";
    RECORDS_UPDATED = "Record(s) is/are updated.";
    OBJECT_ID = "$oid"
