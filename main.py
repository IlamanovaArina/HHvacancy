import os

from src.classes import HeadHunterAPI, Vacancy, JSONSaver

path_data_from_hh = "../HHvacancies/data/vacancies.json"
file_data_from_hh = os.path.abspath(path_data_from_hh)

# path_file_converted_vacancies = "../HHvacancies/data/converted_vacancies.json"
# file_converted_vacancies = os.path.abspath(path_file_converted_vacancies)


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

print(1, hh_api.params)
hh_api.load_vacancies("Python")
print(2, hh_api.params)
print(3, hh_api.vacancies)

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies()

print(4, hh_vacancies)

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

print(5, vacancies_list[0])

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "Умный", "Требования: опыт работы от 3 лет...", "__", 212)

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver(file_data_from_hh)
print(6,json_saver.file_worker)

json_saver.add_vacancy(vacancy)
print(7, json_saver.add_vacancy(vacancy))

json_saver.delete_vacancy(vacancy)
print(8, json_saver.delete_vacancy(vacancy))


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
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()