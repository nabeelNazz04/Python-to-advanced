# vehicle_inheritance.py

# Base class
class Vehicle:
    def gen_usage(self):
        print("General usage: Transportation")

# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self):
        print("I am a car")
    
    def spec_usage(self):
        self.gen_usage()
        print("Specific usage: Family trip")

# Bike class inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self):
        print("I am a bike")
    
    def spec_usage(self):
        print("Specific usage: Solo ride")

# Instantiate and demonstrate Bike functionality
b = Bike()
b.gen_usage()
b.spec_usage()

# Instantiate and demonstrate Car functionality
c = Car()
c.spec_usage()
