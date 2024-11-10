from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        """ Запрос get и запись в vacancies инфы по вакансии """
        pass


class JSONABC(ABC):

    def open_json(self):
        pass

    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass


class VacancyABC:

    @abstractmethod
    @classmethod
    def cast_to_object_list(cls, vacancies: list):
        pass

    @abstractmethod
    def to_dict(self):
        pass
