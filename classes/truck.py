from classes.vehicle import *
class Truck(Vehicle):
    def __init__(self,license_plate,year,max_load):
        super().__init__(license_plate,year)
        self.max_load = max_load

    def calculate_annual_tax(self):
        if self.max_load >= 10:
            year = self.get_year()
            if 2025 - year >= 19:
                print('the tax is 2500')
            else:
                print('the tax is 2000')
        else:
            print('the tax is 1500')
