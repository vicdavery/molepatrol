import unittest
from optical_encoder import Encoder
from motor import Motor

class EncoderTestCase(unittest.TestCase):
    """
    This test is designed to monitor the optical encoders which are tied to the motors. We need to be able to check
    for forward and reverse motion
    """
    forward_pattern = [1,3,4,2]
    backward_pattern = [1,2,3,4]

    def testStaticData(self):
        """
        The encoder should know how many signals it will produce per revolution
        """
        self.assertEqual(Encoder.get_signals_per_revolution(), 1000)

    @unittest.skip("Long running")
    def testEncoderInput1(self):
        # We check what we receive from the first input when the motor turns.
        m = Motor()
        e = Encoder()
        m.forward()
        self.assertTrue(e.get_input(1))
        m.stop()
        m.backward()
        self.assertTrue(e.get_input(1))

    @unittest.skip("Long running")
    def testEncoderInput2(self):
        # Check what we receive from the second encoder input when the motor turns.
        m = Motor()
        e = Encoder()
        m.forward()
        self.assertTrue(e.get_input(2))
        m.stop()
        m.backward()
        self.assertTrue(e.get_input(2))

    @unittest.skip("Long running")
    def testEncoderForward(self):
        # The combination of the 2 inputs provide a 0-3 binary count, the sequence in which the values
        # appear indicates the direction of the motor.
        m = Motor()
        e = Encoder()
        m.forward()
        values = []
        for x in range(100):
            values.append(e.get_value())
        m.stop()




