# import the Pet class
from pet import Pet
def main():
    # information in Pet class
    cute_pet = Pet()
    # title of the system
    print("+----------------------------------------+")
    print("|   LOVE MY PET CLINIC: RECORD SYSTEM    |")
    print("+----------------------------------------+")
    # asks the user to enter the name, type, and age of his or her pet
    name_of_pet = input("Enter your pet's name: ")
    pet_type = input("Specify the type of pet you own: ")
    pet_age = int(input("Enter your pet's age: "))