import unittest
from optical_encoder import Encoder
from motor import Motor

class EncoderTestCase(unittest.TestCase):
    """
    This test is designed to monitor the optical encoders which are tied to the motors. We need to be able to check
    for forward and reverse motion, and running at various speeds.
    """
    def testEncoderInput1(self):
        # We check what we receive from the first input when the motor turns.
        None
    def testEncoderInput2(self):
        # Check what we receive from the second encoder input when the motor turns.
        None
    def testForwardOneRevolution(self):
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
