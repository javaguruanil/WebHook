use webHook_DEV;
db.JOBS_SITE.drop()
db.EDU_COURSE_PRODIVERS.drop()
db.ONLINE_LEARN_RESOURCES.drop()
db.COVID19_EMPLOYMENT_PRGM.drop()
db.VACANCIES.drop()
db.TRAINING.drop()
db.ACCREDITED.drop()
db.NON_ACCREDITED.drop()
db.createCollection("JOBS_SITE", {autoIndexId:true}); 
db.createCollection("EDU_COURSE_PROVIDERS", {autoIndexId:true});
db.createCollection("ONLINE_LEARN_RESOURCES", {autoIndexId:true});
db.createCollection("COVID19_EMPLOYMENT_PRGM", {autoIndexId:true});
db.createCollection("VACANCIES", {autoIndexId:true});
db.createCollection("TRAINING", {autoIndexId:true});
db.createCollection("ACCREDITED", {autoIndexId:true});
db.createCollection("NON_ACCREDITED", {autoIndexId:true});