from enum import Enum
import RPi.GPIO as GPIO

class Patroller_GPIO(object):

    # This Enum will encapsulate the pins used for various functions. Therefore if we need to rewire this
    # is all that should need changing.
    class Pins(Enum):
        motor_1_direction = 17
        motor_1_pwm = 2
        motor_1_current = 4
        motor_1_encoder_1 = 18
        motor_1_encoder_2 = 23
        motor_1_encoder_combined = 6
        motor_2_direction = 22
        motor_2_pwm = 2
        motor_2_current = 27
        motor_2_encoder_1 = 24
        motor_2_encoder_2 = 25
        motor_2_encoder_combined = 6

    def __init__(self):
        # Initialise the pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Pins.motor_1_direction, GPIO.OUT)
        GPIO.setup(Pins.motor_1_current, GPIO.OUT)
        GPIO.setup(Pins.motor_2_direction, GPIO.OUT)
        GPIO.setup(Pins.motor_3_current, GPIO.OUT)
        GPIO.setup(Pins.motor_1_encoder_1, GPIO.IN)
        GPIO.setup(Pins.motor_1_encoder_2, GPIO.IN)
        GPIO.setup(Pins.motor_2_encoder_1, GPIO.IN)
        GPIO.setup(Pins.motor_2_encoder_2, GPIO.IN)

    def fwd(self):
        GPIO.output(Pins.motor_1_direction, True)
        GPIO.output(Pins.motor_2_direction, True)
        GPIO.output(Pins.motor_1_current, True)
        GPIO.output(Pins.motor_2_current, True)
        time.sleep(0.5)
        GPIO.output(Pins.motor_1_current, False)
        GPIO.output(Pins.motor_2_current, False)

    def bckwd(self):
        GPIO.output(Pins.motor_1_direction, False)
        GPIO.output(Pins.motor_2_direction, False)
        GPIO.output(Pins.motor_1_current, True)
        GPIO.output(Pins.motor_2_current, True)
        time.sleep(0.5)
        GPIO.output(Pins.motor_1_current, False)
        GPIO.output(Pins.motor_2_current, False)

    def set_high(self, pin): pass
    def set_low(self, pin): pass

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

