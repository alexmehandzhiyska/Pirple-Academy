class Vehicle:
    def __init__(self, make, model, year, weight, needs_maintenance = False, trips_since_maintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

    def set_make(self, make):
        self.make = make
    
    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year
    
class Cars(Vehicle):
    def __init__(self, make, model, year, weight, needs_maintenance = False, trips_since_maintenance = 0):
        Vehicle.__init__(self, make, model, year, weight, needs_maintenance, trips_since_maintenance)
        self.isDriving = False

    def drive(self):
        self.isDriving = True

    def stop(self):
        self.isDriving = False
        self.trips_since_maintenance += 1

        if self.trips_since_maintenance == 101:
            self.needs_maintenance = True

    def repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False
