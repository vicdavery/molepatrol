from molepatrol.hardware.patroller_gpio import Patroller_GPIO

class Motor(object):
    """
    The Motor class represents a motor, and provides the interface required for driving it.
    The only abilities it has are to run the motor forward or backward at various rates.
    Anything more sophisticated will be controlled by higher level classes.
    """
    def __init__(self, motor_pins):
        self.gpio = Patroller_GPIO()
        self.motor_pins = motor_pins
        self.gpio.set_low(self.motor_pins.current)
        self.gpio.set_low(self.motor_pins.direction)
        self.gpio.set_low(self.motor_pins.pwm)

    def forward(self, rate):
        self.gpio.set_high(self.motor_pins.pwm)

    def backward(self, rate):
        self.gpio.set_low(self.motor_pins.direction)

    def stop(self):
        self.gpio.set_off(self.motor_pins.current)


