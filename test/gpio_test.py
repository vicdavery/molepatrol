import unittest
from enum import Enum
import patroller_gpio

class GPIOTestCase(unittest.TestCase):

    def testMotor1Output(self):
        g = patroller_gpio.PatrollerGPIO()
        self.assertTrue(g.high(patroller_gpio.PatrollerGPIO.Pins.motor_1)

    def testMotor2Output(self):
        self.assertTrue(g.high(patroller_gpio.PatrollerGPIO.Pins.motor_2)

    def testMotor1CurrentSensor(self):pass
    def testMotor2CurrentSensor(self):pass
    def testOpticalEncoder1(self): pass
    def testOpticalEncoder2(self): pass

