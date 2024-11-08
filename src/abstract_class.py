from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        """ Запрос get и запись в vacancies инфы по вакансии """
        pass
