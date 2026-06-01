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
    # data should be stored as the object’s attributes using mutators
    cute_pet.set_name(name_of_pet)
    cute_pet.set_animal_type(pet_type)
    cute_pet.set_age(pet_age)
    print("")
    # retrieve the pet’s name, type, and age and display this data on the screen using accessor
    print("[ RECORDED PET INFORMATION ]")
    print("  > Pet Name    :", cute_pet.get_name())
    print("  > Type of Pet :", cute_pet.get_animal_type())
    print("  > Pet Age     :", cute_pet.get_age(), "years old")
#run
if __name__ == "__main__":
    main()
