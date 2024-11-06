import json

import requests

from src.abstract_class import Parser


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = [] # Вся информация по вакансии из hh.ru

    def load_vacancies(self, keyword):
        """ Запрос get и запись в vacancies инфы по вакансии """
        self.params['text'] = keyword
        # super().load_vacancies(keyword)


    #     self.params['text'] = keyword
    #     while self.params.get('page') != 20:
    #         response = requests.get(self.url, headers=self.headers, params=self.params)
    #         vacancies = response.json()['items']
    #         self.vacancies.extend(vacancies)
    #         self.params['page'] += 1

    def get_vacancies(self):
        """Получение вакансий с hh.ru в формате JSON """
        response = requests.get(self.url, headers=self.headers, params=self.params)

        # if response.status_code == 200:
        #     vacancies = response.json()['items']

        return response

        # with open(self.file_worker, "r+", encoding="utf-8") as file:
        #     print(12, type(file.readlines()))
        #     print(13, file.readlines())
        #
        #     return file.readlines()


class Vacancy:

    def __init__(self, name: str, alternate_url: str, requirement: str, responsibility: str, schedule: str, salary: int):
        self.name = name
        self.alternate_url = alternate_url
        self.requirement = requirement # snippet
        self.responsibility = responsibility # snippet
        self.schedule = schedule # schedule - name
        self.salary = salary # salary - from

        self.dict_vacancy = {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
            "schedule": self.schedule,
            "salary": self.salary,
        }

    def cast_to_object_list(self):
        """  Преобразование набора данных из JSON в список объектов """
        try:
            vacancies = self
            if vacancies.status_code == 200:
                vacancies_list = vacancies.json()['items']
                # print(17, vacancies_list)
                return vacancies_list
            elif vacancies.status_code != 200:
                print("Или нету интернета или какая-то ошибка")
        except Exception as e:
            print(f"Ошибка: {e}")

    def salary_comparisons(self):
        """ Для сравнения вакансий между собой по зарплате и валидировать данные,
        которыми инициализируются его атрибуты. """
        pass


class JSONSaver:

    def __init__(self, file_worker):
        self.file_worker = file_worker


    def add_vacancy(self, vacancy):
        print(15, vacancy.dict_vacancy)
        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(vacancy.dict_vacancy, file)
            print("ok")

    def delete_vacancy(self, vacancy):
        pass

