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