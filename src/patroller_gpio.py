from enum import Enum
import RPi.GPIO as GPIO

class Patroller_GPIO(object):

    # This Enum will encapsulate the pins used for various functions. Therefore if we need to rewire this
    # is all that should need changing.
    class Pins(Enum):
        motor_1_direction = 1
        motor_1_pwm = 2
        motor_1_current = 3
        motor_1_encoder_1 = 4
        motor_1_encoder_2 = 5
        motor_1_encoder_combined = 6
        motor_2_direction = 1
        motor_2_pwm = 2
        motor_2_current = 3
        motor_2_encoder_1 = 4
        motor_2_encoder_2 = 5
        motor_2_encoder_combined = 6

    def __init__(self):
        # Initialise the pins

    def high(self, pin):
        if self.is_input(pin):
            return GPIO.input(pin)
    def set_high(self, pin):
        if self.is_output(pin):
            GPIO.output(pin, True)
    def set_low(self, pin):
        if self.is_output(pin):
            GPIO.output(pin, False)
    def is_input(self, pin):
        return GPIO.pin_function(pin) == GPIO.INPUT
    def is_output(self, pin):
        return GPIO.pin_function(pin) == GPIO.OUTPUT
    def value(self, pin):
        if self.is_input(pin):
            return GPIO.input(pin)

