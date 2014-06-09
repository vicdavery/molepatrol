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
	GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Patroller_GPIO.Pins.motor_1_direction.value, GPIO.OUT)
        GPIO.setup(Patroller_GPIO.Pins.motor_1_current.value, GPIO.OUT)
        GPIO.setup(Patroller_GPIO.Pins.motor_2_direction.value, GPIO.OUT)
        GPIO.setup(Patroller_GPIO.Pins.motor_2_current.value, GPIO.OUT)
        GPIO.setup(Patroller_GPIO.Pins.motor_1_encoder_1.value, GPIO.IN)
        GPIO.setup(Patroller_GPIO.Pins.motor_1_encoder_2.value, GPIO.IN)
        GPIO.setup(Patroller_GPIO.Pins.motor_2_encoder_1.value, GPIO.IN)
        GPIO.setup(Patroller_GPIO.Pins.motor_2_encoder_2.value, GPIO.IN)

    def fwd(self):
        GPIO.output(Patroller_GPIO.Pins.motor_1_direction.value, True)
        GPIO.output(Patroller_GPIO.Pins.motor_2_direction.value, True)
        GPIO.output(Patroller_GPIO.Pins.motor_1_current.value, True)
        GPIO.output(Patroller_GPIO.Pins.motor_2_current.value, True)
        time.sleep(0.5)
        GPIO.output(Patroller_GPIO.Pins.motor_1_current.value, False)
        GPIO.output(Patroller_GPIO.Pins.motor_2_current.value, False)

    def bckwd(self):
        GPIO.output(Patroller_GPIO.Pins.motor_1_direction.value, False)
        GPIO.output(Patroller_GPIO.Pins.motor_2_direction.value, False)
        GPIO.output(Patroller_GPIO.Pins.motor_1_current.value, True)
        GPIO.output(Patroller_GPIO.Pins.motor_2_current.value, True)
        time.sleep(0.5)
        GPIO.output(Patroller_GPIO.Pins.motor_1_current.value, False)
        GPIO.output(Patroller_GPIO.Pins.motor_2_current.value, False)

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

