class EduCourseProvidersFetch():
    def __init__(self,
                 _id,
                 courses,
                 provider_address,
                 schedule_cost,
                 further_info,
                 create_date,
                 update_date,
                 soft_delete):
        self._id = _id
        self.courses = courses
        self.provider_address = provider_address
        self.schedule_cost = schedule_cost
        self.further_info = further_info
