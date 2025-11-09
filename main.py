from classes.electrccar import *
from classes.truck import *
from classes.car import *
from classes.engine import *
if __name__ == '__main__':
    engine = Engine('12',2000)
    engine1 = Engine(13,1500)
    elecriccar = ElectricCar('1234',1999,engine)
    truck = Truck(2345,2020,11)
    car = Car(5678,1800,engine1)
    list = [car,truck,elecriccar]
    for car in list:
        car.calculate_annual_tax()
    car.set_year(9000)
    print(car.get_year())
    elecriccar.get_luxury_features()
    elecriccar.charge()