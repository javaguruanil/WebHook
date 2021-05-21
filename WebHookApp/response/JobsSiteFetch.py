class JobsSiteFetch():
    def __init__(self, _id, job_category, corresponding_job_site, create_date, update_date, soft_delete):
        self._id = _id
        self.job_category = job_category
        self.corresponding_job_site = corresponding_job_site
        # self.create_date = create_date
        # self.update_date = update_date
        # self.soft_delete = soft_delete

# {'_id': {'$oid': '60a6e6d28a3a6bb7b0813e18'},
#  'job_category': 'AAA',
#  'corresponding_job_site': 'BBB',
#  'create_date': '20/05/2021 23:46:42',
#  'update_date': '20/05/2021 23:46:42',
#  'soft_delete': 'No'
#  }
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age