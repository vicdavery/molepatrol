from enum import Enum
#from RPi.GPIO import Hardware
from RPi import GPIO

class Motor_0_Pins(Enum):
    direction = 17
    pwm = 2
    current = 4
    encoder1 = 18
    encoder2 = 23
    encoder_combined = 6

class Motor_1_Pins(Enum):
    direction = 22
    pwm = 2
    current = 27
    encoder1 = 24
    encoder2 = 25
    encoder_combined = 6

class Patroller_GPIO(object):

    def __init__(self):
        # Initialise the pins
        GPIO.Hardware.cleanup()
        GPIO.Hardware.setmode(GPIO.Hardware.BCM)
        GPIO.Hardware.setup(Motor_0_Pins.direction, GPIO.Hardware.OUT)
        GPIO.Hardware.setup(Motor_0_Pins.current, GPIO.Hardware.OUT)
        GPIO.Hardware.setup(Motor_0_Pins.pwm, GPIO.Hardware.OUT)
#        Hardware.setup(Patroller_GPIO.Pins.motor_2_direction.value, Hardware.OUT)
#        Hardware.setup(Patroller_GPIO.Pins.motor_2_current.value, Hardware.OUT)
#        Hardware.setup(Patroller_GPIO.Pins.motor_1_encoder_1.value, Hardware.IN)
#        Hardware.setup(Patroller_GPIO.Pins.motor_1_encoder_2.value, Hardware.IN)
#        Hardware.setup(Patroller_GPIO.Pins.motor_2_encoder_1.value, Hardware.IN)
#        Hardware.setup(Patroller_GPIO.Pins.motor_2_encoder_2.value, Hardware.IN)
#
#    def fwd(self):
#        Hardware.output(Patroller_GPIO.Pins.motor_1_direction.value, True)
#        Hardware.output(Patroller_GPIO.Pins.motor_2_direction.value, True)
#        Hardware.output(Patroller_GPIO.Pins.motor_1_current.value, True)
#        Hardware.output(Patroller_GPIO.Pins.motor_2_current.value, True)
#        time.sleep(0.5)
#        Hardware.output(Patroller_GPIO.Pins.motor_1_current.value, False)
#        Hardware.output(Patroller_GPIO.Pins.motor_2_current.value, False)
#
#    def bckwd(self):
#        Hardware.output(Patroller_GPIO.Pins.motor_1_direction.value, False)
#        Hardware.output(Patroller_GPIO.Pins.motor_2_direction.value, False)
#        Hardware.output(Patroller_GPIO.Pins.motor_1_current.value, True)
#        Hardware.output(Patroller_GPIO.Pins.motor_2_current.value, True)
#        time.sleep(0.5)
#        Hardware.output(Patroller_GPIO.Pins.motor_1_current.value, False)
#        Hardware.output(Patroller_GPIO.Pins.motor_2_current.value, False)
#
#    def high(self, pin):
#        if self.is_input(pin):
#            return Hardware.input(pin)
    def set_high(self, pin):
        if self.is_output(pin):
            GPIO.Hardware.output(pin, True)
    def set_low(self, pin):
        if self.is_output(pin):
            GPIO.Hardware.output(pin, False)
    def is_input(self, pin):
        return GPIO.Hardware.pin_function(pin) == GPIO.Hardware.IN
    def is_output(self, pin):
        return GPIO.Hardware.pin_function(pin) == GPIO.Hardware.OUT
#    def value(self, pin):
#        if self.is_input(pin):
#            return Hardware.input(pin)
#
