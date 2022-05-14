from selenium import webdriver
from selenium.webdriver.common.by import By

from unittest import TestCase
from parameterized import parameterized


class TestSalaryCalc(TestCase):
    URL = "http://192.168.1.135:7000/salary_calc"
    driver = None
    employee_input = None
    calc_button = None
    salary_output = None

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        cls.driver.get(cls.URL)

        cls.employee_input = cls.driver.find_elements(By.ID, 'employeeName')[0]
        cls.calc_button = cls.driver.find_elements(By.ID, 'calcButton')[0]
        cls.salary_output = cls.driver.find_elements(By.ID, 'salaryBudget')[0]

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    @classmethod
    def __get_budget(cls, name):
        cls.employee_input.send_keys(name)
        cls.calc_button.click()
        cls.driver.implicitly_wait(3)
        cls.salary_output = cls.driver.find_elements(By.ID, 'salaryBudget')[0]
        budget = cls.salary_output.get_attribute("value")
        return float(budget)

    @parameterized.expand([
        ["Mykola",  1690],
        ["Antonina", 1608.75],
        ["Snir", 1706.9],
    ])
    def test_employee_salary(self, name, expected_salary):
        actual_salary = self.__get_budget(name)
        self.assertEqual(expected_salary, actual_salary,)
