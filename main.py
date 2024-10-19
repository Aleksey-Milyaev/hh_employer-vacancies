import json
import os.path

from src.employer_vacancy import EmployerVacancy
from config import DATA_DIR


def main():
    """Главная функция"""
    user_input_menu = input("Привет, предлагаю посмотреть вакансии от работодателей, которых я отобрал. Для "
                            "продолжения нажмите enter, чтобы выйти введите 'exit'")

    if user_input_menu == '':
        path = os.path.join(DATA_DIR, 'employers_id.json')
        with open(path, encoding='UTF8') as file:
            content = file.read()
            employers_id = json.loads(content)
        for id_ in employers_id:
            all_vacancy = EmployerVacancy(id_)
            all_vacancy.get_employer_vacancy()
            print(all_vacancy.all_vacancy)


if __name__ == "__main__":
    main()
