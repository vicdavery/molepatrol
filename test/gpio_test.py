import unittest
from suite import TestSettings
from enum import Enum
from patroller_gpio import Patroller_GPIO

class GPIOTestCase(unittest.TestCase):
    def setUp(self):
        if TestSettings.use_mocks:
            self.gpio = unittest.mock.Mock(spec=['input'], side_effect=[True])
        else:
            self.gpio = RPi.GPIO()

    def testMotor1Output(self):
        g = Patroller_GPIO(self.gpio)
        self.assertTrue(g.high(Patroller_GPIO.Pins.motor_out_1))

    def testMotor2Output(self):
        g = Patroller_GPIO(self.gpio)
        self.assertTrue(g.high(Patroller_GPIO.Pins.motor_out_2))

    def testMotor1CurrentSensor(self):pass
    def testMotor2CurrentSensor(self):pass
    def testOpticalEncoder1(self): pass
    def testOpticalEncoder2(self): pass

