from src.Vacancy import Vacancy
from src.class_HH import HeadHunterAPI


def filter_vacancies(vacancies_list, filter_words):
    """Фильтрация вакансий по ключевому слову"""
    filter_list_new = []
    for word in filter_words:
        for vac in vacancies_list:
            if word in vac.get("requirement"):
                filter_list_new.append(vac)
    return filter_list_new


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    salary_list = salary_range.split("-")
    # print(salary_list)
    new_list = []
    for vac in filtered_vacancies:
        if int(salary_list[0]) <= vac["salary"] <= int(salary_list[1]):
            new_list.append(vac)
    return new_list


def sort_vacancies(vacancies_list):
    sorted_vacancies = sorted(vacancies_list, key=lambda vacancies_list: vacancies_list["salary"], reverse=True)
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """Топ вакансий"""
    if top_n == '':
        return sorted_vacancies
    else:
        return sorted_vacancies[0:int(top_n)]


def print_vacancies(top_vacancies):
    dict_vac = []
    for vac in top_vacancies:
        dict_vac.append(f"\nВакансия: {vac.get("name")}\n"
                        f"Ссылка: {vac.get("alternate_url")}\n"
                        f"Зарплата: {vac.get("salary")}\n"
                        f"Требования: {vac.get("requirement")}\n"
                        f"Ответственность: {vac.get("responsibility")}\n"
                        f"График: {vac.get("schedule")}\n"
                        f"{'--'*20}")

    print(*dict_vac)


if __name__ == "__main__":
    # hh_api = HeadHunterAPI()
    #
    # hh_vacancies = hh_api.load_vacancies("Python")
    #
    # vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    # # for d in vacancies_list:
    # #     print(d.get("requirement"))
    # # print(vacancies_list[9:15])
    # sorted_vacancies = filter_vacancies(vacancies_list, "разработчик")
    # get_top_vacancies(sorted_vacancies, "5")
    # filter_vacancies(vacancies_list, ["Python"])
    # print(get_vacancies_by_salary(vacancies_list, "100000 - 150000"))
    # print(len(get_vacancies_by_salary(vacancies_list, "100000 - 150000")))
    top_vacancies = [
        {'name': 'Инженер-программист', 'alternate_url': 'https://hh.ru/vacancy/108682550', 'salary': 300000,
         'requirement': 'Опыт работы с API (JSON). Навыки программирования на одном из языков: <highlighttext>Python</highlighttext>, JavaScript, PHP. Желание создавать эффективные и удобные интеграционные...',
         'responsibility': 'Разработка интеграций для различных платформ и приложений. Настройка и оптимизация API взаимодействий с нашим сервисом. Тестирование и внедрение новых решений...',
         'schedule': 'Удаленная работа'},
        {'name': 'ML-инженер', 'alternate_url': 'https://hh.ru/vacancy/110128119', 'salary': 150000,
         'requirement': 'Знание <highlighttext>Python</highlighttext> и JavaScript, опыт работы с библиотеками для обработки текста (TensorFlow, PyTorch, spaCy, NLTK, Hugging Face Transformers). ',
         'responsibility': 'Разработка и внедрение системы для анализа текстовых данных и персонализации объектов по уникальным характеристикам. Разработка сервиса для сбора и согласования...',
         'schedule': 'Гибкий график'},
        {'name': 'Web-программист', 'alternate_url': 'https://hh.ru/vacancy/110383949', 'salary': 120000,
         'requirement': 'Знания: <highlighttext>Python</highlighttext>, Django, HTML, CSS, SQL, JavaScript, jQuery, Ajax, XML, JSON. Опыт работы с Nginx. Навыки верстки под современные браузеры...',
         'responsibility': 'Разработка высоконагруженных web-проектов.', 'schedule': 'Полный день'},
        {'name': 'Prompt-engineer', 'alternate_url': 'https://hh.ru/vacancy/108689213', 'salary': 100000,
         'requirement': 'Опыт в разработке. Будет плюсом: Знание <highlighttext>Python</highlighttext>/JavaScript. Опыт работы с моделями различной размерности 7b, 70b. ',
         'responsibility': 'Разработка и настройка чат-ботов на основе LLM в визуальном редакторе. Построение логики работы чат-ботов в соответствии с требованиями...',
         'schedule': 'Полный день'},
        {'name': 'Стажер-разработчик', 'alternate_url': 'https://hh.ru/vacancy/108583614', 'salary': 100000,
         'requirement': 'Знание основ программирования. Знания любого языка программирования (JavaScript, PHP, <highlighttext>Python</highlighttext>, C#, Java, C, C++ и др). Писать код, понимать основные...',
         'responsibility': 'Разработка, развитие и поддержка Аналитической системы.', 'schedule': 'Полный день'},
        {'name': 'Тестировщик QA/AQA (middle, senior, удалённо)', 'alternate_url': 'https://hh.ru/vacancy/110336167',
         'salary': 80000,
         'requirement': 'Разрабатывать новые и поддерживать существующие функциональные автотесты (<highlighttext>Python</highlighttext>/Java/C#/JavaScript/Ruby). Продвинутые знания: <highlighttext>Python</highlighttext>, PyTest, Selenium. Опыт и навыки...',
         'responsibility': 'Топ-7 студия по России по работе с некоммерческими и гос.организациями. Функциональным, регрессионным и интеграционным тестированием. Участвовать в организации и...',
         'schedule': 'Полный день'},
        {'name': 'QA-тестировщик /QA engineer (Middle/Senior)', 'alternate_url': 'https://hh.ru/vacancy/110240273',
         'salary': 80000,
         'requirement': 'Опыт настройки автотестов на языках, таких как <highlighttext>Python</highlighttext>, Java или JavaScript. Навыки работы с инструментами автоматизации, например, Selenium, Appium, и...',
         'responsibility': 'Настройка и улучшение процессов тестирования:', 'schedule': 'Полный день'}]
    print_vacancies(top_vacancies)
