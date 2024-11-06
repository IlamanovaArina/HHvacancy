# from urllib import response

import requests
from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
    #     """ Запрос get и запись в vacancies инфы по вакансии """
    #     self.params['text'] = keyword
    #     while self.params.get('page') != 5:
    #         response = requests.get(url='https://api.hh.ru/vacancies',
    #                                 headers={'User-Agent': 'HH-User-Agent'},
    #                                 params=self.params
    #                                 )
    #         vacancies = response.json()['items']
    #         self.vacancies.extend(vacancies)
    #         self.params['page'] += 1



    pass

    # @abstractmethod
    # def add_vacancy(self):
    #     """ Для добавления вакансии """
    #     pass
    #
    # @abstractmethod
    # def delite_vacancy(self):
    #     """ Для удаления вакансии """
    #     pass
    #
    # def filter_vacancy(self):
    #     """ Для фильтрации вакансии по ??? """
    #     pass
