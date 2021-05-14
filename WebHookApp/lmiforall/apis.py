import requests
BASE_URL = "http://api.lmiforall.org.uk/api/v1/"
HEADERS = {'Content-type': 'application/json', 'Accept': 'application/json'}

class Courses:
    GET_COURSES = "courses/courses"
    
    @staticmethod
    def get_courses(subject, postcode=None, distance=None, providers=None, starting_after=None, starting_before=None):
        PARAMS = {
            'subject': subject
        }
        if postcode != None:
            PARAMS['postcode'] = postcode
        if distance != None:
            PARAMS['distance'] = distance
        if providers != None:
            PARAMS['providers'] = providers
        if starting_after != None:
            PARAMS['starting_after'] = starting_after
        if starting_before != None:
            PARAMS['starting_before'] = starting_before
        
        res = requests.get(url = BASE_URL + Courses.GET_COURSES, params = PARAMS, headers=HEADERS)
        return res.json()

class Vacancies:
    GET_VACANCIES = "vacancies/search"

    @staticmethod
    def get_vacancies(keywords, location=None, radius=None, limit=None):
        # MAX limit is set to 50 by the LMI website
        PARAMS = {
                'keywords': keywords
        }
        if location != None:
            PARAMS['location'] = location
        if radius != None:
            PARAMS['radius'] = radius
        if limit != None:
            PARAMS['limit'] = limit

        res = requests.get(url = BASE_URL + Vacancies.GET_VACANCIES, params = PARAMS, headers=HEADERS)
        return res.json()

if __name__ == "__main__":
    print(Vacancies.get_vacancies("software engineer"))
