import unittest

class BatteryMonitorTestCase(unittest.TestCase):
    def testFullyCharged(self):
        self.assertEqual(BatteryMonitor().get_charge(), BatteryMonitor.FULLY_CHARGED)

    def testDrainRateReport(self):
        b = BatteryMonitor()
        self.assertGreater(b.get_drain_rate(), 0, "Drain rate must be more than 0 otherwise we would not be using any battery")
        self.assertLess(b.get_drain_rate(), 10, "There is a limit to how much battery we can drain")

    def testCurrentCharge(self):
        b = BatteryMonitor()
        self.assertLessEqual(b.get_charge(), BatteryMonitor.FULLY_CHARGED, "Except at initial turn on, or while on the charger, the battery will never be fully charged")

    def testTimeRemaining(self):
        b = BatteryMonitor()
        # Time remaining will be somewhere between 1 and 599 minutes
        self.assertGreater(b.get_charge(), 0, "We cannot have 0 minutes remaining otherwise we would be dead")
        self.assertLess(b.get_charge(), 600, "The battery cannot last >= 10 hours")
if __name__ == '__main__':
    unittest.main()

