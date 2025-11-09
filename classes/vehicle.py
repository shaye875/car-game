from abc import *
class Vehicle:
    def __init__(self,license_plate,year):
        self.__license_plate = license_plate
        self.__year = year

    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self,num):
        self.__license_plate = num

    def get_year(self):
        return self.__year

    def set_year(self,num):
        self.__year = num

    @abstractmethod
    def calculate_annual_tax(self):
        pass