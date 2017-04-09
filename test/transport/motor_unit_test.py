import unittest
from optical_encoder import Encoder
from motor_unit import MotorUnit

class MotorUnitTestCase(unittest.TestCase):
    """
    The motor unit is a combination of the motor and the optical encoder.
    """
    def testForwardOneRevolution(self):
        """
        How do we know we've gone forward one revolution?
        By knowing how many what the output for the optical encoder would look like.
        The encoder must know what how many changed inputs it should receive to indicate
        a full revolution.
        m = MotorUnit()
        """
        None
    def testReverseOneRevolution(self):
        None
    def testForwardFast(self):
        None
    def testReverseFast(self):
        None
    def testForwardMedium(self):
        None
    def testReverseMedium(self):
        None
    def testForwardSlow(self):
        None
    def testReverseSlow(self):
        None
