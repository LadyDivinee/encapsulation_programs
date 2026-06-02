#class
class Pet:
    # pet class should have an _ _init_ _ method
    def __init__(self):
        # for the name of a pet
        self.__name = ""
        # for the type of animal that a pet is
        self.__animal_type = ""
        # for the pet’s age
        self.__age = 0
    # setter method
    def set_name(self, name):
        self.__name = str(name)

    def set_animal_type(self, animal_type):
        self.__animal_type = str(animal_type)

    def set_age(self, age):
        self.__age = int(age)