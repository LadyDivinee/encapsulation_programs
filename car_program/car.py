#class named Car
class Car:
    #an _ _init_ _ method that accepts the car’s year model and make as arguments
    def __init__(self, year_model, make):
        #private members
        self.__year_model = str(year_model)
        self.__make = str(make)
        self.__speed = 0
        #methods
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed
