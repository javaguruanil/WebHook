from flask import Flask, jsonify, request, render_template, make_response

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

@app.route("/index")
def index():
    return render_template("index.html")

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

@app.route("/render/jobsSite/save")
def jobsSiteSavePage():
    return render_template("jobsSiteSave.html")

@app.route("/render/jobsSite/fetch")
def jobsSiteFetchPage():
    return render_template("jobsSiteFetch.html")

@app.route("/render/jobsSite/udpate")
def jobsSiteUpdatePage():
    return render_template("jobsSiteUpdate.html")

@app.route("/render/jobsSite/delete")
def jobsSiteDeletePage():
    return render_template("jobsSiteDelete.html")

######################## Accredited ######################################
@app.route("/render/accredited/save")
def accreditedSavePage():
    return render_template("accreditedSave.html")

@app.route("/render/accredited/fetch")
def accreditedFetchPage():
    return render_template("accreditedFetch.html")

@app.route("/render/accredited/udpate")
def accreditedUpdatePage():
    return render_template("accreditedUpdate.html")

@app.route("/render/accredited/delete")
def accreditedDeletePage():
    return render_template("accreditedDelete.html")
######################## Non Accredited ######################################
@app.route("/render/nonAccredited/save")
def nonAccreditedSavePage():
    return render_template("nonAccreditedSave.html")

@app.route("/render/nonAccredited/fetch")
def nonAccreditedFetchPage():
    return render_template("nonAccreditedFetch.html")

@app.route("/render/nonAccredited/udpate")
def nonAccreditedUpdatePage():
    return render_template("nonAccreditedUpdate.html")

@app.route("/render/nonAccredited/delete")
def nonAccreditedDeletePage():
    return render_template("nonAccreditedDelete.html")

######################## Education Course Providers ######################################
@app.route("/render/edu/course/providers/save")
def eduCourseProvidersSavePage():
    return render_template("eduCourseProvidersSave.html")

@app.route("/render/edu/course/providers/fetch")
def eduCourseProvidersFetchPage():
    return render_template("eduCourseProvidersFetch.html")

@app.route("/render/edu/course/providers/udpate")
def eduCourseProvidersUpdatePage():
    return render_template("eduCourseProvidersUpdate.html")

@app.route("/render/edu/course/providers/delete")
def eduCourseProvidersDeletePage():
    return render_template("eduCourseProvidersDelete.html")

######################## Online Learning Resources ######################################
@app.route("/render/online/learning/resources/save")
def onlineLearningResourcesSavePage():
    return render_template("onlineLearningResourcesSave.html")

@app.route("/render/online/learning/resources/fetch")
def onlineLearningResourcesFetchPage():
    return render_template("onlineLearningResourcesFetch.html")

@app.route("/render/online/learning/resources/udpate")
def onlineLearningResourcesUpdatePage():
    return render_template("onlineLearningResourcesUpdate.html")

@app.route("/render/online/learning/resources/delete")
def onlineLearningResourcesDeletePage():
    return render_template("onlineLearningResourcesDelete.html")

######################## Covid19 Employment Pgm ######################################
@app.route("/render/covid19/employment/pgm/save")
def covid19EmploymentPgmSavePage():
    return render_template("covid19EmploymentPgmSave.html")

@app.route("/render/covid19/employment/pgm/fetch")
def covid19EmploymentPgmFetchPage():
    return render_template("covid19EmploymentPgmFetch.html")

@app.route("/render/covid19/employment/pgm/udpate")
def covid19EmploymentPgmUpdatePage():
    return render_template("covid19EmploymentPgmUpdate.html")

@app.route("/render/covid19/employment/pgm/delete")
def covid19EmploymentPgmDeletePage():
    return render_template("covid19EmploymentPgmDelete.html")

######################## Vacancies ######################################
@app.route("/render/vacancies/save")
def vacanciesSavePage():
    return render_template("vacanciesSave.html")

@app.route("/render/vacancies/fetch")
def vacanciesFetchPage():
    return render_template("vacanciesFetch.html")

@app.route("/render/vacancies/udpate")
def vacanciesUpdatePage():
    return render_template("vacanciesUpdate.html")

@app.route("/render/vacancies/delete")
def vacanciesDeletePage():
    return render_template("vacanciesDelete.html")

####################### START:: MONGODB CODE ############################################
###### START :: Save operations #######
@app.route("/save/jobSites", methods = ["POST"])
def save_job_sites() :
    return render_template("index.html", msg=saveJobsSite(request.form.to_dict()))

@app.route("/save/edu/course/providers", methods = ["POST"])
def save_edu_course_providers() :
    return render_template("index.html", msg=saveEducationCourseProviders(request.form.to_dict()))

@app.route("/save/online/learning/resources", methods = ["POST"])
def save_online_learn_resources() :
    return render_template("index.html", msg=saveOnlineLearnResources(request.form.to_dict()))

@app.route("/save/covid19/employment/pgm", methods = ["POST"])
def save_covid19_employment_pgm() :
    return render_template("index.html", msg=saveCovid19EmploymentPgm(request.form.to_dict()))

@app.route("/save/vacancies", methods = ["POST"])
def save_vacancies() :
    return render_template("index.html", msg=saveVacancies(request.form.to_dict()))

@app.route("/save/training", methods = ["POST"])
def save_training() :
    return jsonify(saveTraining(request.json))

@app.route("/save/accredited", methods = ["POST"])
def save_accredited() :
    return render_template("index.html", msg=saveAccredited(request.form.to_dict()))

@app.route("/save/nonAccredited", methods = ["POST"])
def save_non_accredited() :
    return render_template("index.html", msg=saveNonAccredited(request.form.to_dict()))

###### END :: Save operations #######

##### START :: GET operations ######
@app.route("/fetch/jobSites", methods = ["GET"])
def fetch_job_sites() :
    return render_template("jobsSiteDisplayPage.html", msg=fetchJobsSite(request.args.to_dict()))

@app.route("/fetch/edu/course/providers", methods = ["GET"])
def fetch_edu_course_providers() :
    return render_template("eduCourseProvidersDisplayPage.html", msg=fetchEducationCourseProviders(request.args.to_dict()))

@app.route("/fetch/online/learning/resources", methods = ["GET"])
def fetch_online_learning_resources() :
    return render_template("onlineLearningResourcesDisplayPage.html", msg=fetchOnlineLearnResources(request.args.to_dict()))

@app.route("/fetch/covid19/employment/pgm", methods = ["GET"])
def fetch_covid19_employment_pgm() :
    return render_template("covid19EmploymentPgmDisplayPage.html", msg=fetchCovid19EmploymentPgm(request.args.to_dict()))

@app.route("/fetch/vacancies", methods = ["GET"])
def fetch_vacancies() :
    return render_template("vacanciesDisplayPage.html", msg=fetchVacancies(request.args.to_dict()))

@app.route("/fetch/training", methods = ["GET"])
def fetch_training() :
    return fetchTraining(request.args.to_dict())

@app.route("/fetch/accredited", methods = ["GET"])
def fetch_accredited() :
    return render_template("accreditedDisplayPage.html", msg=fetchAccredited(request.args.to_dict()))

@app.route("/fetch/nonAccredited", methods = ["GET"])
def fetch_non_accredited() :
    return render_template("nonAccreditedDisplayPage.html", msg=fetchNonAccredited(request.args.to_dict()))
##### END :: GET operations ######


##### START :: SOFT DELETE operations ######
@app.route("/delete/jobSites", methods = ["GET"])
def delete_job_sites() :
    return render_template("index.html",msg=deleteJobsSite(request.args.get("_id")))

@app.route("/delete/edu/course/providers", methods = ["GET"])
def delete_edu_course_providers() :
    return render_template("index.html",msg=deleteEducationCourseProviders(request.args.get("_id")))

@app.route("/delete/online/learning/resources", methods = ["GET"])
def delete_online_learning_resources() :
    return render_template("index.html",msg=deleteOnlineLearnResources(request.args.get("_id")))

@app.route("/delete/covid19/employment/pgm", methods = ["GET"])
def delete_covid19_employment_pgm() :
    return render_template("index.html",msg=deleteCovid19EmploymentPgm(request.args.get("_id")))

@app.route("/delete/vacancies", methods = ["GET"])
def delete_vacancies() :
    return render_template("index.html",msg=deleteVacancies(request.args.get("_id")))

@app.route("/delete/training", methods = ["GET"])
def delete_training() :
    return deleteTraining(id)

@app.route("/delete/accredited", methods = ["GET"])
def delete_accredited() :
    return render_template("index.html",msg=deleteAccredited(request.args.get("_id")))

@app.route("/delete/nonAccredited", methods = ["GET"])
def delete_non_accredited() :
    return render_template("index.html",msg=deleteNonAccredited(request.args.get("_id")))
##### END :: SOFT DELETE operations ######

##### START :: UPDATE operations ######
@app.route("/update/jobSites", methods = ["POST"])
def update_job_sites() :
    return render_template("index.html",msg=updateJobsSite(request.form.to_dict()))

@app.route("/update/edu/course/providers", methods = ["POST"])
def update_edu_course_providers() :
    return render_template("index.html",msg=updateEducationCourseProviders(request.form.to_dict()))

@app.route("/update/online/learning/resources", methods = ["POST"])
def update_online_learning_resources() :
    return render_template("index.html",msg=updateOnlineLearnResources(request.form.to_dict()))

@app.route("/update/covid19/employment/pgm", methods = ["POST"])
def update_covid19_employment_pgm() :
    return render_template("index.html",msg=updateCovid19EmploymentPgm(request.form.to_dict()))

@app.route("/update/vacancies", methods = ["POST"])
def update_vacancies() :
    return render_template("index.html",msg=updateVacancies(request.form.to_dict()))

@app.route("/update/training", methods = ["POST"])
def update_training() :
    return updateTraining(request.json)

@app.route("/update/accredited", methods = ["POST"])
def update_accredited() :
    return render_template("index.html",msg=updateAccredited(request.form.to_dict()))

@app.route("/update/nonAccredited", methods = ["POST"])
def update_non_accredited() :
    return render_template("index.html",msg=updateNonAccredited(request.form.to_dict()))
##### END :: UPDATE operations ######

########################## END:: MONGODB CODE #########################################
if __name__ == "__main__":
    app.run()
