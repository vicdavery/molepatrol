import unittest
import time
from motor import Motor


class MotorTestCase(unittest.TestCase):
    def testForward(self):
        # At this level of abstraction, the only indicator we'll have that the motor has run at all
        # is visual feedback of the motor.
        # Once we combine the optical encoder in a "MotorUnit" then we will be able to determine
        # distance turned and speed, etc.
        m = Motor()
        m.forward()
        time.sleep(1)
        m.stop()

    def testBackward(self):
        m = Motor()
        m.backward()
        time.sleep(1)
        m.stop()

