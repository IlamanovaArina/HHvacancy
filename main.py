import os

from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy
from src.class_HH import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, sort_vacancies, print_vacancies

path_data_from_hh = "../HHvacancies/data/vacancies.json"
file_data_from_hh = os.path.abspath(path_data_from_hh)

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.load_vacancies("Python")
# for d in hh_vacancies:
#     print(d.get("description"))
# print(hh_vacancies[0:10])

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# print(vacancies_list[0:5])

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...", "1", 10000)

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
# print(json_saver.delete_vacancy(vacancy))


# print(json_saver.add_vacancy(vacancy))


# Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n) # (sorted_vacancies, top_n)
#     print(len(top_vacancies))
#     print(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()