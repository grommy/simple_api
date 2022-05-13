from unittest import TestCase

from core.employee import Employee


class TestSalaryCalc(TestCase):

    def test_100_salary(self):
        salary_100 = Employee("mykola", "t", 100)
        self.assertEqual(1690, salary_100.get_annual_salary_budget())

    def test_low_salary(self):
        low_salary = Employee("antonina", "t", 99)
        self.assertEqual(1608.75, low_salary.get_annual_salary_budget())

    def test_high_salary(self):
        low_salary = Employee("Olha", "t", 101)
        self.assertEqual(1706.9, low_salary.get_annual_salary_budget())
