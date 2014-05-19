import unittest
import unittest.mock
import time
from motor import Motor
from battery_monitor import BatteryMonitor
from suite import TestSettings

class MotorTestCase(unittest.TestCase):

    def testForward100Percent(self):
        m = Motor()
        m.forward(100)
        self.assertGreater(m.current_drain(), 0, "The current drain should not be 0 when the motor is running")

    def testBackward100Percent(self):
        m = Motor()
        m.backward(100)
        self.assertGreater(m.current_drain(), 0, "The current drain should not be 0 when the motor is running")

    def testForward50Percent(self):
        m = Motor()
        m.forward(50)
        self.assertGreater(m.current_drain(), 0, "The current drain should not be 0 when the motor is running")

    def testBackward50Percent(self):
        m = Motor()
        m.backward(50)
        self.assertGreater(m.current_drain(), 0, "The current drain should not be 0 when the motor is running")

    def testCurrentIncreaseWithHigherOutput(self):
        m = Motor()
        m.forward(20)
        drain = m.current_drain()
        self.assertGreater(drain, 0, "The current drain should not be 0 when the motor is running")
        m.forward(40)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 40% than at 20%")
        drain = m.current_drain()
        m.forward(60)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 60% than at 40%")
        drain = m.current_drain()
        m.forward(80)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 80% than at 60%")
        drain = m.current_drain()
        m.forward(100)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 100% than at 80%")
        m.stop()

