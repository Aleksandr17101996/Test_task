import requests
from config import Base


class NewUser(Base):
    url = Base.BASE_URL

    """Библиотека api"""

    def create_user(self, name):
        """Метод добавляет нового пользователя и возвращает id созданного пользователя"""

        data = {
            "Name": name
        }
        r = requests.post(self.url + "CreateUser", json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_user(self, user_id):
        """Метод предоставляет информацию о пользователе найденному по id"""

        data = {
            "id": user_id
        }
        r = requests.get(self.url + "GetUser", json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def set_user_age(self, user_id, age):
        """Метод добавляет информацию о возрасте пользователю найденного по id"""

        data = {
            "id": user_id,
            "Age": age
        }
        r = requests.post(self.url + "SetUserAge", json=data)
        status_code = r.status_code
        return status_code

    def get_age_group(self, user_id):
        """Метод предоставляет информацию о возрастной группе пользователе найденному по id"""

        r = requests.get(self.url + user_id + "/GetAgeGroupById")
        status_code = r.status_code
        body = r.json()
        return status_code, body




