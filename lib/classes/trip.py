class Trip:
    all=[]
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_start_date):
        if isinstance(new_start_date, str) and len(new_start_date) >=7:
            self._start_date = new_start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_end_date):
        if isinstance(new_end_date, str) and len(new_end_date) >= 7:
            self._end_date = new_end_date

from classes.national_park import NationalPark
from classes.visitor import Visitor