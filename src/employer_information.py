import json
from abc import ABC, abstractmethod

import requests


class HHEmployee(ABC):
    """Абстрактный метод для вывода информации об работодателе"""
    @abstractmethod
    def get_employee_information(self):
        pass


class EmployerInformation(HHEmployee):
    """Класс получения информации работодателя"""
    def __init__(self, employer_id: int):
        """Инициализатор класса EmployerInformation"""
        self.url = f"https://api.hh.ru/employers/{employer_id}"
        self.information = []

    def get_employee_information(self):
        """Функция получения информации работодателя"""
        try:
            response = requests.get(url=self.url).text
            information = json.loads(response)
            information_dict = dict(id=information['id'], name=information['name'], type=information['type'],
                                    area=information['area']['name'], open_vacancies=information['open_vacancies'])
            self.information.append(information_dict)
        except ConnectionError:
            print("Ошибка соединения")

