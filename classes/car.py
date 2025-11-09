from classes.vehicle import *
class Car(Vehicle):
    def __init__(self,license_plate,year,engine):
        super().__init__(license_plate,year)
        self.engine = engine

    def calculate_annual_tax(self):
        year = self.get_year()
        power = self.engine.horsepower
        if 2025 - year >= 19:
            if power > 1600:
                print('the tax is 2000')
            else:
                print('the tax is 1500')
        else:
            print('the tax is 1200')