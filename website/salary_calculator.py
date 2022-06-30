from .models import Worker, Project, Pms, PmsSalary, Entity, Subdiv, Wage, Accrual1C
from . import db
import datetime, calendar


class Calculator:
    def __init__(self, month, year):
        self.month = None
        self.year = None
        self.db = db
        self.days = self.evaluate_days()

    def evaluate_days(self):
        num_days = calendar.monthrange(self.year, self.month)[1]
        return [datetime.date(self.year, self.month, day) for day in range(1, num_days+1)]

    def pms(self):
        pms_rows = Pms.query.filter(Pms.date in self.days)
        for row in pms_rows:
            if row.overhr > row.total:
