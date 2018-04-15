class Vehicle(object):
    def speed(self):
        print('it is a low speed vehicle')
    def slow(self):
        print('its moving very slow')
class Car(Vehicle):
    def parts(self):
        print('ringa ringa ')
    def brand(self):
        print('mandara puvvalle pusindi')
class Bike(Vehicle):
    def hero(self):
        print('this is hero honda bike')
    def suzuki(self):
        print('this is suzuki car')

run=Bike()
sit=Car()

run.speed()
run.slow()
sit.parts()
sit.brand()
sit.speed()
sit.slow()
