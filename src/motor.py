from patroller_gpio import Patroller_GPIO as GPIO
class Motor(object):
    """
    The Motor class represents a motor, and provides the interface required for driving it.
    The only abilities it has are to run the motor forward or backward. Anything more sophisticated will
    be controlled by higher level classes.
    """

    def __init__(self, motor_id, motor_sensor_id):
        self.gpio = GPIO()
        self.motor_id = motor_id
        self.motor_sensor_id = motor_sensor_id
        self.gpio.set_low(self.motor_id)

    def forward(self, rate):
        self.gpio.set_high(self.motor_id)

    def backward(self, rate):
        self.gpio.set_low(self.motor_id)

    def stop(self):
        self.gpio.set_off(self.motor_id)

    def current_drain(self):
        return self.gpio.value(self.motor_sensor_id)

