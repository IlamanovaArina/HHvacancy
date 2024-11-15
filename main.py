from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy
from src.class_HH import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, sort_vacancies, print_vacancies

if __name__ == "__main__":
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    search_query: str = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies: list = hh_api.load_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list: list[dict] = Vacancy.cast_to_object_list(hh_vacancies)

    # Функция для взаимодействия с пользователем
    def user_interaction():
        """ Функция для взамиодействия с пользователем """
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words: list = input("Введите ключевые слова для фильтрации вакансий: ").split()
        salary_range: str = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

        filtered_vacancies: list = filter_vacancies(vacancies_list, filter_words)

        ranged_vacancies: list = get_vacancies_by_salary(filtered_vacancies, salary_range)

        sorted_vacancies: list = sort_vacancies(ranged_vacancies)
        top_vacancies: list = get_top_vacancies(sorted_vacancies, top_n)

        print_vacancies(top_vacancies)

        # Пример работы контструктора класса с одной вакансией
        vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", 10000,
                          "Требования: опыт работы от 3 лет...", "Ответственность: ...", "Полный день")

        # Сохранение информации о вакансиях в файл
        json_saver = JSONSaver(top_vacancies)
        json_saver.writing_data_to_file()
        json_saver.add_vacancy(vacancy)
        json_saver.delete_vacancy(vacancy)

    user_interaction()
