import dataclasses

SALARY_LOW_THRESHOLD = 100
TAX_RATE_LOW = 0.25
TAX_RATE_HIGH = 0.3


@dataclasses.dataclass
class Employee:
    name: str
    position: str
    monthly_salary: float

    def get_annual_salary_budget(self):
        if self.monthly_salary < SALARY_LOW_THRESHOLD:
            tax_rate = TAX_RATE_LOW
        else:
            tax_rate = TAX_RATE_HIGH

        return self.monthly_salary * 13 * (1 + tax_rate)

