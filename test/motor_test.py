import unittest
import unittest.mock
import time
from motor import Motor
from battery_monitor import BatteryMonitor
from suite import TestSettings

class MotorTestCase(unittest.TestCase):
    def testForward(self):
        # At this level of abstraction, there are precious few indicators, so
        # we'll use a combination of battery drain and the pin that is set with a value.
        bm = BatteryMonitor()
        b = None
        if TestSettings.use_mocks:
            b = unittest.mock.Mock(spec=bm.get_drain_rate, side_effect=[5,10,5])
        else:
            b = bm.get_drain_rate
        m = Motor()
        dr = b()
        m.forward()
        self.assertNotEqual(m.forward_pin, 0)
        self.assertEqual(m.backward_pin, 0)
        time.sleep(1)
        self.assertGreater(b(), dr, msg="Battery drain rate should be greater when the motor is running")
        m.stop()
        self.assertEqual(m.forward_pin, 0)
        self.assertEqual(m.backward_pin, 0)
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
        self.assertEqual(m.forward_pin, 0)
        self.assertNotEqual(m.backward_pin, 0)
        time.sleep(1)
        self.assertGreater(b(), dr, msg="Battery drain rate should be greater when the motor is running")
        m.stop()
        self.assertEqual(m.forward_pin, 0)
        self.assertEqual(m.backward_pin, 0)
        self.assertAlmostEqual(b(), dr, msg="Battery drain rate should be return to normal when the motor stops running")

