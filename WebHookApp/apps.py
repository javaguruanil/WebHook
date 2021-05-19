from flask import Flask, jsonify, request

from WebHookApp.mongoDb.Accredited import saveAccredited, fetchAccredited, deleteAccredited, updateAccredited
from WebHookApp.mongoDb.Covid19EmployementPrgm import saveCovid19EmploymentPgm, fetchCovid19EmploymentPgm, \
    deleteCovid19EmploymentPgm, updateCovid19EmploymentPgm
from WebHookApp.mongoDb.EducationCourseProviders import saveEducationCourseProviders, fetchEducationCourseProviders, \
    deleteEducationCourseProviders, updateEducationCourseProviders
from WebHookApp.mongoDb.JobsSite import saveJobsSite, fetchJobsSite, deleteJobsSite, updateJobsSite
from WebHookApp.mongoDb.NonAccredited import saveNonAccredited, fetchNonAccredited, deleteNonAccredited, \
    updateNonAccredited
from WebHookApp.mongoDb.OnlineLearningResource import saveOnlineLearnResources, fetchOnlineLearnResources, \
    deleteOnlineLearnResources, updateOnlineLearnResources
from WebHookApp.mongoDb.Training import saveTraining, fetchTraining, deleteTraining, updateTraining
from WebHookApp.mongoDb.Vacancies import saveVacancies, fetchVacancies, deleteVacancies, updateVacancies
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

###### END :: Save operations #######

##### START :: GET operations ######
@app.route("/fetch/jobSites", methods = ["GET"])
def fetch_job_sites() :
    return fetchJobsSite(request.args.to_dict())

@app.route("/fetch/edu/course/providers", methods = ["GET"])
def fetch_edu_course_providers() :
    return fetchEducationCourseProviders(request.args.to_dict())

@app.route("/fetch/online/learning/resources", methods = ["GET"])
def fetch_online_learning_resources() :
    return fetchOnlineLearnResources(request.args.to_dict())

@app.route("/fetch/covid19/employment/pgm", methods = ["GET"])
def fetch_covid19_employment_pgm() :
    return fetchCovid19EmploymentPgm(request.args.to_dict())

@app.route("/fetch/vacancies", methods = ["GET"])
def fetch_vacancies() :
    return fetchVacancies(request.args.to_dict())

@app.route("/fetch/training", methods = ["GET"])
def fetch_training() :
    return fetchTraining(request.args.to_dict())

@app.route("/fetch/accredited", methods = ["GET"])
def fetch_accredited() :
    return fetchAccredited(request.args.to_dict())

@app.route("/fetch/nonAccredited", methods = ["GET"])
def fetch_non_accredited() :
    return fetchNonAccredited(request.args.to_dict())
##### END :: GET operations ######


##### START :: SOFT DELETE operations ######
@app.route("/delete/jobSites/<id>", methods = ["DELETE"])
def delete_job_sites(id) :
    return deleteJobsSite(id)

@app.route("/delete/edu/course/providers/<id>", methods = ["DELETE"])
def delete_edu_course_providers(id) :
    return deleteEducationCourseProviders(id)

@app.route("/delete/online/learning/resources/<id>", methods = ["DELETE"])
def delete_online_learning_resources(id) :
    return deleteOnlineLearnResources(id)

@app.route("/delete/covid19/employment/pgm/<id>", methods = ["DELETE"])
def delete_covid19_employment_pgm(id) :
    return deleteCovid19EmploymentPgm(id)

@app.route("/delete/vacancies/<id>", methods = ["DELETE"])
def delete_vacancies(id) :
    return deleteVacancies(id)

@app.route("/delete/training/<id>", methods = ["DELETE"])
def delete_training(id) :
    return deleteTraining(id)

@app.route("/delete/accredited/<id>", methods = ["DELETE"])
def delete_accredited(id) :
    return deleteAccredited(id)

@app.route("/delete/nonAccredited/<id>", methods = ["DELETE"])
def delete_non_accredited(id) :
    return deleteNonAccredited(id)
##### END :: SOFT DELETE operations ######

##### START :: UPDATE operations ######
@app.route("/update/jobSites", methods = ["POST"])
def update_job_sites() :
    return updateJobsSite(request.json)

@app.route("/update/edu/course/providers", methods = ["POST"])
def update_edu_course_providers() :
    return updateEducationCourseProviders(request.json)

@app.route("/update/online/learning/resources", methods = ["POST"])
def update_online_learning_resources() :
    return updateOnlineLearnResources(request.json)

@app.route("/update/covid19/employment/pgm", methods = ["POST"])
def update_covid19_employment_pgm() :
    return updateCovid19EmploymentPgm(request.json)

@app.route("/update/vacancies", methods = ["POST"])
def update_vacancies() :
    return updateVacancies(request.json)

@app.route("/update/training", methods = ["POST"])
def update_training() :
    return updateTraining(request.json)

@app.route("/update/accredited", methods = ["POST"])
def update_accredited() :
    return updateAccredited(request.json)

@app.route("/update/nonAccredited", methods = ["POST"])
def update_non_accredited() :
    return updateNonAccredited(request.json)
##### END :: UPDATE operations ######

########################## END:: MONGODB CODE #########################################
if __name__ == "__main__":
    app.run()
