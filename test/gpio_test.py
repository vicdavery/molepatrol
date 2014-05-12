import unittest
from suite import TestSettings
from enum import Enum
from patroller_gpio import Patroller_GPIO

class GPIOTestCase(unittest.TestCase):

    def testMotor1Output(self):
        gpio = None
        if TestSettings.use_mocks:
            gpio = unittest.mock.Mock(spec=['input'], side_effect=[True])
        else:
            gpio = RPi.GPIO()
        g = Patroller_GPIO(gpio)
        self.assertTrue(g.high(Patroller_GPIO.Pins.motor_sensor_1))

    def testMotor2Output(self):
        gpio = None
        if TestSettings.use_mocks:
            gpio = unittest.mock.Mock(spec=['input'], side_effect=[True])
        else:
            gpio = RPi.GPIO()
        g = Patroller_GPIO(gpio)
        self.assertTrue(g.high(Patroller_GPIO.Pins.motor_sensor_2))

    def testMotor1CurrentSensor(self):pass
    def testMotor2CurrentSensor(self):pass
    def testOpticalEncoder1(self): pass
    def testOpticalEncoder2(self): pass

