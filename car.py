#class named Car
class Car:
    #an _ _init_ _ method that accepts the car’s year model and make as arguments
    def __init__(self, year_model, make):\
        #private members
        self.__year_model = str(year_model)
        self.__make = str(make)
        self.__speed = 0