class NationalPark:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 3< len(new_name) and not hasattr(self, "name"):
            self._name = new_name
    
    def trips(self):
        trips= []
        for obj in Trip.all:
            if obj.national_park == self:
                trips.append(obj)
        return trips
    
    def visitors(self):
        visitors=[]
        for obj in Trip.all:
            if obj.national_park == self:
                visitors.append(obj.visitor)
        return list(set(visitors))
    
    def total_visits(self):
        total=0
        for obj in Trip.all:
            if obj.national_park == self:
                total += 1
        return total
    
    def best_visitor(self):
        visitors=[]
        for obj in Trip.all:
            if obj.national_park == self:
                visitors.append(obj.visitor)
        return max(set(visitors), key=visitors.count)
       

    
        
        

from classes.trip import Trip