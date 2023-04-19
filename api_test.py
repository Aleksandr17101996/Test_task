import random
from faker import Faker

from api import NewUser

fake = Faker()


class TestAgeGroup:
    class TestApi(NewUser):
        """Проверяем работу каждого из доступных api запросов"""

        def test_new_user(self):
            """Проверяем возможность создания нового пользователя"""

            name = fake.name
            status_code, body = self.create_user(name)
            assert status_code == 201, "Статус кода не соответсвует"
            assert len(body["id"]) > 0, "id пользователя некорректен"
            return body["id"]

        def test_get_user(self):
            """Проверяем возможность предостовления информации о пользователе"""

            user_id = self.test_new_user()
            status_code, body = self.get_user(user_id)
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert "Name" in body

        def test_set_user_age(self):
            """Проверяем возможность добавления данных о возрасте пользователя"""

            user_id = self.test_new_user()
            age = random.randint(0, 100)
            status_code = self.set_user_age(user_id, age)
            assert status_code == 200, "Статус кода не соответствует ожидаемому"

        def test_get_age_group(self):
            """Проверяем возможность предоставлении данных по возрастной группе пользователя"""

            user_id = self.test_new_user()
            status_code, body = self.get_age_group(user_id)
            assert status_code == 200, "Статус кода несоответсвует ожидаемому"
            assert "AgeGroup" in body

    class TestFunctional(TestApi):
        """Проверяем правильность работы функционала приложения"""

        def test_age_group_young(self):
            """Проdереям правильность определения возрастной группы Young """
            _, body = self.create_user("Jey")
            id_user = body['id']
            self.set_user_age(id_user, 0)
            status_code, body = self.get_age_group(id_user)
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert body["AgeGroup"] == "Young"

        def test_age_group_yong(self):
            """Проdереям правильность определения возрастной группы Young """
            _, body = self.create_user("Андрей")
            id_user = body['id']
            self.set_user_age(id_user, 18)
            status_code, body = self.get_age_group(id_user)
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert body["AgeGroup"] == "Young"

        def test_age_group_adult(self):
            """Проdереям правильность определения возрастной группы Adult """
            _, body = self.create_user("Иван")
            id_user = body['id']
            self.set_user_age(id_user, 19)
            status_code, body = self.get_age_group(id_user)
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert body["AgeGroup"] == "Abult", "Ошибка определения группы"

        def test_age_adult(self):
            """Проdереям правильность определения возрастной группы Adult """

            _, body = self.create_user("Иван")
            id_user = body['id']
            self.set_user_age(id_user, 100)
            status_code, body = self.get_age_group(id_user)
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert body["AgeGroup"] == "Adult", "Ошибка определении группы"
