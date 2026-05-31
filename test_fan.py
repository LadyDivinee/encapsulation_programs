#import Fan class
from fan import Fan
#setter method
def main():
    # assign the maximum speed, radius 10, color yellow, and turn it on
    first_fan = Fan()
    first_fan.set_speed(Fan.FAST)
    first_fan.set_radius(10)
    first_fan.set_color("yellow")
    first_fan.set_on(True)
    # Assign medium speed, radius 5, color blue, and turn it off 
    second_fan = Fan()
    second_fan.set_speed(Fan.MEDIUM)
    second_fan.set_radius(5)
    second_fan.set_color("blue")
    second_fan.set_on(False)