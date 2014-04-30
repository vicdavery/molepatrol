import unittest
import unittest.mock
import time
from motor import Motor
from battery_monitor import BatteryMonitor
from suite import TestSettings

class MotorTestCase(unittest.TestCase):
    def testForward(self):
        # At this level of abstraction, the only indicator we'll have that the motor has run at all
        # is the drain rate on the battery.
        # Once we combine the optical encoder in a "MotorUnit" then we will be able to determine
        # distance turned and speed, etc.
        bm = BatteryMonitor()
        b = None
        if TestSettings.use_mocks:
            b = unittest.mock.Mock(spec=bm.get_drain_rate, side_effect=[5,10,5])
        else:
            b = bm.get_drain_rate
        m = Motor()
        dr = b()
        m.forward()
        time.sleep(1)
        self.assertGreater(b(), dr, msg="Battery drain rate should be greater when the motor is running")
        m.stop()
        self.assertAlmostEqual(b(), dr, msg="Battery drain rate should be return to normal when the motor stops running")

    def testBackward(self):
        bm = BatteryMonitor()
        b = None
        if TestSettings.use_mocks:
            b = unittest.mock.Mock(spec=bm.get_drain_rate, side_effect=[5,10,5])
        else:
            b = bm.get_drain_rate
        m = Motor()
        dr = b()
        m.backward()
        time.sleep(1)
        self.assertGreater(b(), dr, msg="Battery drain rate should be greater when the motor is running")
        m.stop()
        self.assertAlmostEqual(b(), dr, msg="Battery drain rate should be return to normal when the motor stops running")

