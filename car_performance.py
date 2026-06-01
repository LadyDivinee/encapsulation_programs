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

