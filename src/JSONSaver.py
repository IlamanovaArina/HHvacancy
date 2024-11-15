
import json
import os
from json import JSONDecodeError

from src.Vacancy import Vacancy
from src.abstract_class import JSONABC


class JSONSaver(JSONABC):

    def __init__(self, vacancies_list: list[dict], name: str = "data.json"):
        self.__name = name
        self.path = os.path.join(os.path.dirname(__file__), "..", "data", self.__name)
        self.vacancies_list = vacancies_list

    def open_json(self):
        """ Метод открывающий json-файл, если возникает
        какая-либо ошибка, возвращается пустой список """
        try:
            with open(self.path) as f:
                return json.load(f)
        except JSONDecodeError:
            return []
        except Exception as e:
            print(e)
            return []

    def writing_data_to_file(self):
        vacancy_list = self.open_json()
        new_list = []
        for vacancy_dict in vacancy_list:
            new_list.append(vacancy_dict.get("alternate_url"))
        for vac in self.vacancies_list:
            if vac.get("alternate_url") not in new_list:
                vacancy_list.append(vac)
                with open(self.path, "w") as f:
                    json.dump(vacancy_list, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy):
        """ Метод для добавления вакансии в файл json """
        vacancy_list: list = self.open_json()
        new_list = []
        for vacancy_dict in vacancy_list:
            new_list.append(vacancy_dict.get("alternate_url"))
        if vacancy.alternate_url not in new_list:
            vacancy_list.append(vacancy.to_dict())
            with open(self.path, "w") as file:
                json.dump(vacancy_list, file, ensure_ascii=False, indent=4)
        else:
            return "Данная вакансия уже существует"

    def delete_vacancy(self, vacancy: Vacancy):
        """ Метод для удаления вакансии из json-файла """
        open_json: list = self.open_json()
        new_list_url = []
        for vacancy_dict in open_json:
            new_list_url.append(vacancy_dict.get("alternate_url"))
        if vacancy.alternate_url in new_list_url:
            for i in range(len(open_json)):
                if open_json[i-1]['alternate_url'] == vacancy.alternate_url:
                    del open_json[i-1]
        else:
            return "Вакансия не найдена."

        with open(self.path, "w") as file:
            json.dump(open_json, file, ensure_ascii=False, indent=4)
