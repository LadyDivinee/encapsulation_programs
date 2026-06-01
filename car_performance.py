#import Car class
from car import Car
def main():
    #car's year model and make
    bmw_car = Car("2026", "BMW")
    #header for BMW 2026 performance
    print("+----------------------------------------+")
    print("|           BMW 2026 SIMULATOR           |")
    print("+----------------------------------------+")
    print("  Initial Speed:", bmw_car.get_speed(), "km/h")
    print("")
    #accelerate method five times and get the current speed of the car and display it
    print("[  ACCELERATION  (5 TIMES)   ]")
    for i in range(1, 6):
        bmw_car.accelerate()
        print(f"  > Step {i}: Current Speed is {bmw_car.get_speed()} km/h")
    print("")
    #brake method five times and call to the brake method, get the current speed of the car and display it
    print("[  BRAKING (5 TIMES)  ]")
    for i in range(1, 6):
        bmw_car.brake()
        print(f"  > Step {i}: Current Speed is {bmw_car.get_speed()} km/h")
#run
if __name__ == "__main__":
    main()

