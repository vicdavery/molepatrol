import unittest
from optical_encoder import Encoder
from motor import Motor

class EncoderTestCase(unittest.TestCase):
    """
    This test is designed to monitor the optical encoders which are tied to the motors. We need to be able to check
    for forward and reverse motion
    """
    def testEncoderInput1(self):
        # We check what we receive from the first input when the motor turns.
        m = Motor()
        e = Encoder()
        m.forward()
        self.assertTrue(e.get_input(1))
        m.stop()
        m.backward()
        self.assertTrue(e.get_input(1))

    def testEncoderInput2(self):
        # Check what we receive from the second encoder input when the motor turns.
        m = Motor()
        e = Encoder()
        m.forward()
        self.assertTrue(e.get_input(2))
        m.stop()
        m.backward()
        self.assertTrue(e.get_input(2))
