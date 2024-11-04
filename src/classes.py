import json

import requests


class HeadHunterAPI:
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = [] # Вся информация по вакансии из hh.ru
        self.file_worker = file_worker

    def load_vacancies(self, keyword):
        """ Запрос get и запись в vacancies инфы по вакансии """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def get_vacancies(self):
        """Получение вакансий с hh.ru в формате JSON """
        with open(self.file_worker, "a", encoding="utf-8") as file:
            json.dump(self.vacancies, file)


class Vacancy:

    def __init__(self, name: str, alternate_url: str, requirement: str, responsibility: str, schedule: str, salary: int):
        self.name = name
        self.alternate_url = alternate_url
        self.requirement = requirement # snippet
        self.responsibility = responsibility # snippet
        self.schedule = schedule # schedule - name
        self.salary = salary # salary - from


    def cast_to_object_list(self):

        pass


class JSONSaver:

    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass

