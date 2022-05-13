from unittest import TestCase
import requests
from parameterized import parameterized


class TestSalaryCalc(TestCase):
    URL = "http://127.0.0.1:5000/salary"

    @parameterized.expand([
        ["Mykola",  1690],
        ["Antonina", 1608.75],
        ["Snir", 1706.9],
    ])
    def test_employee_salary(self, name, expected_salary):
        response = self.__get_salary_response(name)
        self.assertEqual(200, response.status_code,)
        resp_json = response.json()
        self.assertEqual(expected_salary, resp_json["annual_salary_budget"],)

    def __get_salary_response(self, name):
        response = requests.get(url=self.URL, params={"name": name})
        return response
