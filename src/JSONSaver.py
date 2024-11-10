from abc import ABC, abstractmethod
from json import JSONDecodeError

from src.Vacancy import Vacancy
import os

import json

# class JSONABC(ABC):

    # @abstractmethod
    # def json_add(self):
    #     pass
    #
    # @abstractmethod
    # def json_del(self):
    #     pass


class JSONSaver:

    def __init__(self, name="data.json"):
        self.name = name
        self.path = os.path.join(os.path.dirname(__file__), "..", "data", self.name)

    def open_json(self):
        try:
            with open(self.path) as f:
                return json.load(f)
        except JSONDecodeError:
            return []
        except Exception as e:
            print(e)
            return []

    def add_vacancy(self, vacancy):
        vacancy_list = self.open_json()
        new_list = []
        for vacancy_dict in vacancy_list:
            new_list.append(vacancy_dict.get("alternate_url"))
        if vacancy.alternate_url not in new_list:
            vacancy_list.append(vacancy.to_dict())
            with open(self.path, "w") as file:
                json.dump(vacancy_list, file, ensure_ascii=False, indent=4)
        else:
            return "Данная вакансия уже существует"

    def delete_vacancy(self, vacancy):
        open_json = self.open_json() # [{}, {}, {}]
        new_list_url = [] # "<grger>"
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


if __name__ == "__main__":
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123479>", "2",
                      "Опыт работы от 3 лет...", "1", "100 000-150 000 руб.")
    obj = JSONSaver("data.json")
    # obj.add_vacancy(vacancy)
    obj.delete_vacancy(vacancy)