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
    CREATE_DATE = "create_date"
    UPDATE_DATE = "update_date"
    SKILL_TYPES = "skill_types"
    SKILL_TYPE = "skill_type"

    # ACCREDITED, NON_ACCREDITED, Training table columns
    BOROUGH = "borough"
    SUBJECT = "subject"
    POSSIBLE_OPTIONS = "possible_options"
    WHERE_TO_FIND_MORE = "where_to_find_more"
    SECTOR_OR_JOB_TYPE = "sector_or_job_type"
    TRAINING_OPTION = "training_option"

    # COVID19_EMPLOYMENT_PRGM, ONLINE_LEARN_RESOURCES table columns
    CORRESPONDING_ONLINE_LINKS = "corresponding_online_links"

    # EDU_COURSE_PROVIDERS, VACANCIES table columns
    COURSES = "courses"
    PROVIDER_ADDRESS = "provider_address"
    SCHEDULE_COST = "schedule_cost"
    FURTHER_INFO = "further_info"
    CAREER_OPTIONS_FOR_SKILLS = "career_options_for_skills"

    # JOBS_SITE table columns
    JOB_CATEGORY = "job_category"
    CORRESPONDING_JOB_SITE = "corresponding_job_site"

    ACCREDITED_DATA_NOT_CREATED = "Accredited data not created."
    ACCREDITED_DATA_CREATED = "Accredited data created."

    COVID19_EMP_PGM_DATA_NOT_CREATED = "Covid19EmploymentPgm data not created."
    COVID19_EMP_PGM_DATA_CREATED = "Covid19EmploymentPgm data created."

    EDU_COURSE_PROVIDERS_DATA_NOT_CREATED = "EducationCourseProviders data not created."
    EDU_COURSE_PROVIDERS_DATA_CREATED = "EducationCourseProviders data created."

    JOBS_SITE_DATA_NOT_CREATED  = "JobsSite data not created."
    JOBS_SITE_DATA_CREATED  = "JobsSite data created."

    NON_ACCREDITED_DATA_NOT_CREATED = "NonAccredited data not created."
    NON_ACCREDITED_DATA_CREATED = "NonAccredited data created."

    ONLINE_LEARN_RESOURCES_DATA_NOT_CREATED = "OnlineLearnResources data not created."
    ONLINE_LEARN_RESOURCES_DATA_CREATED = "OnlineLearnResources data created."

    TRAINING_DATA_NOT_CREATED = "Training data not created."
    TRAINING_DATA_CREATED = "Training data created."

    VACANCIES_DATA_NOT_CREATED = "Vacancies data not created."
    VACANCIES_DATA_CREATED = "Vacancies data created."

    HYPHEN = "-"



