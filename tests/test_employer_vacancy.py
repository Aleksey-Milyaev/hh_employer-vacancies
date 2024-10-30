from src.employer_vacancy import EmployerVacancy
import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def get_employer():
    return EmployerVacancy(123456)


def test_employer_vacation_init(get_employer):
    assert get_employer.url == "https://api.hh.ru/vacancies"
    assert get_employer.params == {"employer_id": 123456, "page": 0, "per_page": 100}
    assert get_employer.headers == {"User-Agent": "HH-User-Agent"}


@patch("requests.get")
def test_get_employee_vacation(mock_get, get_employer):
    mock_response = MagicMock()
    mock_response.json.return_value = {'items': [{'id': '108858682',  'name': 'Web-программист - стажер',  'area':
        {'url': 'https://api.hh.ru/areas/160'}, 'salary': None, 'employer': {'id': '5031522', 'name': 'Autodata'}}]}

    mock_get.return_value = mock_response
    get_employer.get_employer_vacancy()
    assert get_employer.all_vacancy == [('108858682', 'Web-программист - стажер', 'https://api.hh.ru/areas/160',
                                         0, 0, '5031522', 'Autodata')]