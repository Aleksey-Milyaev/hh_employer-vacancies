import json
from abc import ABC, abstractmethod

import requests


class HHApi(ABC):
    """Абстрактный класс получения вакансий"""
    @abstractmethod
    def get_employer_vacancy(self):
        pass


class EmployerVacancy(HHApi):
    """Класс получения вакансий по id работодателя"""
    def __init__(self, employee_id: int):
        """Инициализатор класса EmployerVacancy"""
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"employer_id": employee_id, "page": 0, "per_page": 100}
        self.all_vacancy = []

    def get_employer_vacancy(self):
        """Функция получения вакансий"""
        response = requests.get(url=self.url, headers=self.headers, params=self.params).text
        vacancy = json.loads(response)['items']
        for item in vacancy:
            vacancy_info = dict(id=item['id'], vacancy_name=item['name'], area=item['area']['name'],
                                salary_from=item['salary']['from'] if item['salary'] is not None else 0,
                                salary_to=item['salary']['to'] if item['salary'] is not None else 0,
                                employer_id=item['employer']['id'], employer_name=item['employer']['name'])
            self.all_vacancy.append(vacancy_info)

