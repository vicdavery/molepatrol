import unittest
from battery_monitor import BatteryMonitor
from scarer import Scarer

class ScareSystemTestCase(unittest.TestCase):
    def testScarer(self):
        # Check the battery drain first.
        b = BatteryMonitor()
        dr = b.get_drain_rate()

        # Start the scarer
        s = Scarer()
        s.scare()

        # Battery drain should be higher
        self.assertGreater(dr, b.get_drain_rate(), msg="The battery drain rate should be greater with the scarer running")
        # Stop the scarer
        s.stop_scaring()
        # Battery drain should return to normal
        self.assertAlmostEqual(dr, b.get_drain_rate(), msg="The battery drain rate should return to more or less the same once the scarer stops")

