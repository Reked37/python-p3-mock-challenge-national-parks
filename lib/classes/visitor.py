class Visitor:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1< len(new_name) <15:
            self._name = new_name

    def trips(self):
        trips=[]
        for obj in Trip.all:
            if obj.visitor == self:
                trips.append(obj)
        return trips
    
    def national_parks(self):
        parks=[]
        for obj in Trip.all:
            if obj.visitor == self:
                parks.append(obj.national_park)
        return list(set(parks))
    
    def total_visits_at_park(self, park):
        count=0
        for obj in Trip.all:
            if obj.national_park == park:
                print('worked')
                count+=1
        return count

from classes.trip import Trip
from classes.national_park import NationalPark