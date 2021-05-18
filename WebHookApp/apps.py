from flask import Flask, jsonify, request

from WebHookApp.mongoDb.Accredited import saveAccredited
from WebHookApp.mongoDb.Covid19EmployementPrgm import saveCovid19EmploymentPgm
from WebHookApp.mongoDb.EducationCourseProviders import saveEducationCourseProviders
from WebHookApp.mongoDb.JobsSite import saveJobsSite
from WebHookApp.mongoDb.NonAccredited import saveNonAccredited
from WebHookApp.mongoDb.OnlineLearningResource import saveOnlineLearnResources
from WebHookApp.mongoDb.Training import saveTraining
from WebHookApp.mongoDb.Vacancies import saveVacancies
from lmiforall.apis import *

import logging

app = Flask(__name__)

logging.basicConfig(filename='webhook.log', level=logging.DEBUG, format=f'[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')

@app.route("/")
def hello():
    app.logger.debug("LOGS")
    return "Hello World!"

@app.route("/vacancies")
def get_vacancies():
    keywords = request.args.get('keywords', None)
    location = request.args.get('location', None)
    radius = request.args.get('radius', None)
    limit = request.args.get('limit', None)

    if keywords == None:
        return jsonify({"status":"error", "errorMessage": "Please provide a keyword to search for vacancies"})

    return jsonify(Vacancies.get_vacancies(keywords, location, radius, limit))

@app.route("/courses")
def get_courses():
    subject = request.args.get('subject', None)
    if subject == None:
        return jsonify({"status":"error", "errorMessage": "Please provide a subject to search for cources"})
    postcode = request.args.get('postcode', None)

    return jsonify(Courses.get_courses(subject, postcode))


####################### START:: MONGODB CODE ############################################
###### START :: Save operations #######
@app.route("/save/jobSites", methods = ["POST"])
def save_job_sites() :
    return jsonify(saveJobsSite(request.json))

@app.route("/save/edu/course/providers", methods = ["POST"])
def save_edu_course_providers() :
    return jsonify(saveEducationCourseProviders(request.json))

@app.route("/save/online/learning/resources", methods = ["POST"])
def save_online_learn_resources() :
    return jsonify(saveOnlineLearnResources(request.json))

@app.route("/save/covid19/employment/pgm", methods = ["POST"])
def save_covid19_employment_pgm() :
    return jsonify(saveCovid19EmploymentPgm(request.json))

@app.route("/save/vacancies", methods = ["POST"])
def save_vacancies() :
    return jsonify(saveVacancies(request.json));

@app.route("/save/training", methods = ["POST"])
def save_training() :
    return jsonify(saveTraining(request.json))

@app.route("/save/accredited", methods = ["POST"])
def save_accredited() :
    return jsonify(saveAccredited(request.json))

@app.route("/save/nonAccredited", methods = ["POST"])
def save_non_accredited() :
    return jsonify(saveNonAccredited(request.json))

# ###### END :: Save operations #######

# TODO :: remaining implementation
# ##### START :: GET opertaions ######
# @app.route("/fetch/jobSites", methods = ["GET"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/fetch/edu/course/providers", methods = ["GET"])
# def save_edu_course_providers() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/fetch/online/learning/resources", methods = ["GET"])
# def save_edu_course_providers() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/fetch/covid19/employment/pgm", methods = ["GET"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/fetch/vacancies", methods = ["GET"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/fetch/training", methods = ["GET"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/fetch/accredited", methods = ["GET"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/fetch/nonAccredited", methods = ["GET"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
# ##### END :: GET opertaions ######
#
#
# ##### START :: SOFT DELETE opertaions ######
# @app.route("/delete/jobSites", methods = ["DELETE"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/delete/edu/course/providers", methods = ["DELETE"])
# def save_edu_course_providers() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/delete/online/learning/resources", methods = ["DELETE"])
# def save_edu_course_providers() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/delete/covid19/employment/pgm", methods = ["DELETE"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/delete/vacancies", methods = ["DELETE"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/delete/training", methods = ["DELETE"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/delete/accredited", methods = ["DELETE"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/delete/nonAccredited", methods = ["DELETE"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
# ##### END :: SOFT DELETE opertaions ######
#
#
# ##### START :: UPDATE opertaions ######
# @app.route("/update/jobSites", methods = ["POST"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/update/edu/course/providers", methods = ["POST"])
# def save_edu_course_providers() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/update/online/learning/resources", methods = ["POST"])
# def save_edu_course_providers() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/update/covid19/employment/pgm", methods = ["POST"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/update/vacancies", methods = ["POST"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/update/training", methods = ["POST"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/update/accredited", methods = ["POST"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
#
# @app.route("/update/nonAccredited", methods = ["POST"])
# def save_job_sites() :
#     return "<h1>Hello welcome Raju Mohandu Anil ************* </h1>"
# ##### END :: UPDATE opertaions ######
#
########################## END:: MONGODB CODE #########################################
if __name__ == "__main__":
    app.run()
