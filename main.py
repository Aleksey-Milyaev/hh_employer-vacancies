import json
import os.path

from src.employer_vacancy import EmployerVacancy
from src.employer_information import EmployerInformation
from config import DATA_DIR


def main():
    """Главная функция"""
    user_input_menu = input("Привет, предлагаю посмотреть вакансии от работодателей, которых я отобрал или информацию "
                            "о работодателях. Для просмотра вакансий нажмите 1, для просмотра информации о "
                            "работодателях чтобы выйти введите 'exit'\n")

    path = os.path.join(DATA_DIR, 'employers_id.json')
    with open(path, encoding='UTF8') as file:
        content = file.read()
        employers_id = json.loads(content)

    if user_input_menu == '1':
        for id_ in employers_id:
            all_vacancy = EmployerVacancy(id_)
            all_vacancy.get_employer_vacancy()
            print(all_vacancy.all_vacancy)
    elif user_input_menu == '2':
        for id_ in employers_id:
            employers_information = EmployerInformation(id_)
            employers_information.get_employee_information()
            print(employers_information.information)


if __name__ == "__main__":
    main()
