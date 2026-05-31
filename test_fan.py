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