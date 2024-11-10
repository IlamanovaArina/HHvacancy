class Vacancy:
    name: str
    alternate_url: str
    requirement: str
    responsibility: str
    schedule: str
    salary: int

    __slots__ = ("name", "alternate_url", "salary", "requirement", "responsibility", "schedule")

    def __init__(self, name, alternate_url, requirement, responsibility, schedule, salary):
        self.name = name
        self.alternate_url = alternate_url
        self.salary = self.__validation_salary(salary)
        self.requirement = self.__validation_requirement(requirement)
        self.responsibility = responsibility  # snippet
        self.schedule = schedule  # schedule - name

    def __str__(self):
        return (f"Вакансия: {self.name}\n"
                f"Ссылка: {self.alternate_url}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.requirement}\n"
                f"Ответственность: {self.responsibility}\n"
                f"График: {self.schedule}\n"
                )

    @staticmethod
    def __validation_salary(salary):
        if salary:
            return salary
        return "Не указана"

    @staticmethod
    def __validation_requirement(requirement):
        if requirement:
            return requirement
        return "Не указаны"

    @classmethod
    def cast_to_object_list(cls, vacancies: list):
        new_list = []
        for vacancy in vacancies:
            name = vacancy.get("name")
            alternate_url = vacancy.get("alternate_url")
            if vacancy.get("snippet").get("requirement") is None:
                requirement = "Не указаны"
            else:
                requirement = vacancy.get("snippet").get("requirement")

            if vacancy.get("salary") is None or vacancy.get("salary").get("from") is None:
                salary = 0
            else:
                salary = vacancy.get("salary").get("from")

            if vacancy.get("snippet").get("responsibility") is None:
                responsibility = "Не указано"
            else:
                responsibility = vacancy.get("snippet").get("responsibility")

            if vacancy.get("schedule") is None:
                schedule = "Не указано"
            else:
                schedule = vacancy.get("schedule").get("name")

            dict_vac = {"name": name,
                        "alternate_url": alternate_url,
                        "salary": salary,
                        "requirement": requirement,
                        "responsibility": responsibility,
                        "schedule": schedule,
                        }
            new_list.append(dict_vac)
        return new_list

    def __repr__(self):
        return (f"Вакансия: {self.name}\n"
                f"Ссылка: {self.alternate_url}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.requirement}\n"
                f"Ответственность: {self.responsibility}\n"
                f"График: {self.schedule}\n"
                )

    @classmethod
    def __isinstance_data(cls, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Операнд справа должен быть экземпляром класса Vacancy")
        else:
            return other.salary

    def __eq__(self, other):
        sal_1 = self.__isinstance_data(other)
        return self.salary == sal_1

    def __lt__(self, other):
        sal_2 = self.__isinstance_data(other)
        return self.salary < sal_2

    def __le__(self, other):
        sal_3 = self.__isinstance_data(other)
        return self.salary <= sal_3

    def to_dict(self):
        """Возвращает словарь с данными о вакансии из экземпляра класса Vacancy"""
        return {"name": self.name, "alternate_url": self.alternate_url, "salary": self.salary,
                "requirement": self.requirement}


if __name__ == "__main__":
    ex = Vacancy.cast_to_object_list([{'id': '108858682', 'premium': False,
                                       'name': 'Web-программист - стажер', 'department': None,
                                       'has_test': False, 'response_letter_required': False,
                                       'area': {'id': '160', 'name': 'Алматы', 'url': 'https://api.hh.ru/areas/160'},
                                       'salary': None, 'type': {'id': 'open', 'name': 'Открытая'},
                                       'address': {'city': 'Алматы', 'street': 'бульвар Бухар Жырау',
                                                   'building': '26/1', 'lat': 43.232296, 'lng': 76.923259,
                                                   'description': "Пойдет", 'raw': 'Алматы, бульвар Бухар Жырау, 26/1',
                                                   'metro': None, 'metro_stations': [], 'id': '16504789'},
                                       'response_url': None, 'sort_point_distance': None,
                                       'published_at': '2024-10-18T15:33:27+0300',
                                       'created_at': '2024-10-18T15:33:27+0300', 'archived': False,
                                       'apply_alternate_url':
                                           'https://hh.ru/applicant/vacancy_response?vacancyId=108858682',
                                       'insider_interview': None,
                                       'url': 'https://api.hh.ru/vacancies/108858682?host=hh.ru',
                                       'alternate_url': 'https://hh.ru/vacancy/108858682', 'relations': [],
                                       'employer': {'id': '5031522', 'name': 'Autodata',
                                                    'url': 'https://api.hh.ru/employers/5031522',
                                                    'alternate_url': 'https://hh.ru/employer/5031522',
                                                    'logo_urls': None,
                                                    'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5031522',
                                                    'accredited_it_employer': False, 'trusted': True},
                                       'snippet': {'requirement': 'Знать теорию тестирования, что такое тест планы, '
                                                                  'чек листы и протокол тестирования, свободно владеть ЯП '
                                                                  '<highlighttext>Python</highlighttext>, быть приспособленным к '
                                                                  'монотонной...',
                                                   'responsibility': 'Как правильно работать с git-ом в команде. Писать '
                                                                     'автотесты на базе Selenium/<highlighttext>Python</highlighttext> '
                                                                     '(тестировщик). Создавать web-дизайны для реальных...'},
                                       'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
                                       'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
                                       'accept_temporary': False,
                                       'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                                       'accept_incomplete_resumes': True,
                                       'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
                                       'employment': {'id': 'probation', 'name': 'Стажировка'},
                                       'adv_response_url': None,
                                       'is_adv_vacancy': False, 'adv_context': None}])
    ex2 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                  "Требования: опыт работы от 3 лет...", "График1", 15000, "Описание1")
    ex3 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                  "Требования: опыт работы от 3 лет...", "График2", 10000, "Описание2")
    # print(ex)
    # print(repr(ex2))
    # print(ex3)
    # print(ex2 == ex3)
    # print(ex2 < ex3)
    # print(ex2 <= ex3)
    # print(ex2 != ex3)
    # print(ex2 > ex3)
    # print(ex2 >= ex3)
