import os

from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy
from src.class_HH import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, sort_vacancies, print_vacancies

if __name__ == "__main__":
    path_data_from_hh = "../HHvacancies/data/vacancies.json"
    file_data_from_hh = os.path.abspath(path_data_from_hh)

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Пример работы контструктора класса с одной вакансией
    vacancy1 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                      "Требования: опыт работы от 3 лет...", "1", 10000)
    vacancy2 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123455>", "100 000-150 000 руб.",
                      "Требования: опыт работы от 3 лет...", "1", 10000)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy1)
    json_saver.delete_vacancy(vacancy2)


    # Функция для взаимодействия с пользователем
    def user_interaction():
        platforms = ["HeadHunter"]
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)  # (sorted_vacancies, top_n)
        # print(len(top_vacancies))
        # print(top_vacancies)

        print_vacancies(top_vacancies)


    user_interaction()
