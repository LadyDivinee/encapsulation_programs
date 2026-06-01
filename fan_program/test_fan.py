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
    # Display each object’s speed, radius, color, and on properties
    print("+----------------------------------------+")
    print("|          FIRST FAN PROPERTIES          |")
    print("+----------------------------------------+")
    print("|  > Speed  :", first_fan.get_speed())
    print("|  > Radius :", first_fan.get_radius())
    print("|  > Color  :", first_fan.get_color())
    print("|  > On     :", first_fan.get_on())
    print("+----------------------------------------+")
    print("")
    print("+----------------------------------------+")
    print("|        SECOND FAN PROPERTIES           |")
    print("+----------------------------------------+")
    print("|  > Speed  :", second_fan.get_speed())
    print("|  > Radius :", second_fan.get_radius())
    print("|  > Color  :", second_fan.get_color())
    print("|  > On     :", second_fan.get_on())
    print("+----------------------------------------+")
#run
if __name__ == "__main__":
    main()
