from abc import ABC, abstractmethod


class Parser(ABC):
    """ Абстрактный класс для работы с API HeadHunter """

    @abstractmethod
    def load_vacancies(self, keyword):
        """ Запрос get и запись в vacancies инфы по вакансии """
        pass


class VacancyABC:
    """ Абстрактный класс для работы с полученными
    вакансиями и приведения к определённому виду """

    @classmethod
    @abstractmethod
    def cast_to_object_list(cls, vacancies: list):
        pass

    @abstractmethod
    def to_dict(self):
        pass


class JSONABC(ABC):
    """ Абстрактный класс для работы с Json-файлом """

    def writing_data_to_file(self):
        pass

    def open_json(self):
        pass

    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass
