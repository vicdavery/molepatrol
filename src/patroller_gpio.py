from enum import Enum

class Patroller_GPIO(object):

    # This Enum will encapsulate the pins used for various functions. Therefore if we need to rewire this
    # is all that should need changing.
    class Pins(Enum):
        motor_out_1 = 1
        motor__out_2 = 2
        encorder_1 = 3
        encoder_2 = 4
        combined_encoder = 5
        motor_sensor_1 = 6
        motor_sensor_2 = 7

