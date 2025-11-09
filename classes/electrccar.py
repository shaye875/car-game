from classes.electricmixin import *
from classes.car import *
from classes.luxurymixun import *

class ElectricCar(ElectricMixin,Car,LuxuryMixin):
    def calculate_annual_tax(self):
        print('the tax is 250')