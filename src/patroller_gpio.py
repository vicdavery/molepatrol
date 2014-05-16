from enum import Enum
import RPi.GPIO as GPIO

class Patroller_GPIO(object):

    # This Enum will encapsulate the pins used for various functions. Therefore if we need to rewire this
    # is all that should need changing.
    class Pins(Enum):
        motor_out_1 = 1
        motor_out_2 = 2
        encorder_1 = 3
        encoder_2 = 4
        combined_encoder = 5
        motor_sensor_1 = 6
        motor_sensor_2 = 7
    def high(self, pin):
        return GPIO.input(pin)
    def is_input(self, pin):
        return GPIO.pin_function(pin) == GPIO.INPUT
    def is_output(self, pin):
        return GPIO.pin_function(pin) == GPIO.OUTPUT
