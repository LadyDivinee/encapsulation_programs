#class
class Fan:
    #constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        #private int data field named speed that specifies the speed of the fan
        self.__speed = int(speed)
        #private bool data field named on that specifies whether the fan is on
        self.__on = bool(on)
        #private float data field named radius that specifies the radius of the fan
        self.__radius = float(radius)
        #private string data field named color that specifies the color of the fan
        self.__color = str(color)

    #accessor(getter) method
    def get_speed(self):
        return self.__speed

    def get_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    #mutator(setter) method
    def set_speed(self, speed):
        self.__speed = speed

    def set_on(self, on):
        self.__on = bool(on)

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)


