import dataclasses

TAX_RATE = 0.25


@dataclasses.dataclass
class Employee:
    name: str
    position: str
    monthly_salary: float

    def get_annual_salary_budget(self):
        return (self.monthly_salary * (12 + 1)) * (1 + TAX_RATE)
