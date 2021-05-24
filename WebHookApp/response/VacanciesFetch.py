class VacanciesFetch():
    def __init__(self,
                 _id,
                 skill_type,
                 career_options_for_skills,
                 further_info,
                 create_date,
                 update_date,
                 soft_delete):
        self._id = _id
        self.skill_type = skill_type
        self.career_options_for_skills = career_options_for_skills
        self.further_info = further_info
