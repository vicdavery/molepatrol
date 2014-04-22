import unittest
from motor import Motor

class MotorTestCase(unittest.TestCase):
    def testForwardOneStep(self):
        m = Motor()
        pos = m.get_position()
        m.single_step()
        self.assertGreater(m.get_position(), pos)

    def testBackwardOneStep(self):
        m = Motor()
        pos = m.get_position()
        m.single_step_back()
        self.assertEqual(m.get_position(), Motor.steps_per_revolution - 1)

    def testForwardOneRevolution(self):
        m = Motor()
        pos = m.get_position()
        m.single_step(m.get_steps_per_revolution())
        self.assertEqual(m.get_position(), pos)

    def testBackwardOneRevolution(self):
        m = Motor()
        pos = m.get_position()
        m.single_step_back(m.get_steps_per_revolution())
        self.assertEqual(m.get_position(), pos)

    def testForwardTwoRevolutions(self):
        m = Motor()
        pos = m.get_position()
        m.single_step(m.get_steps_per_revolution()*2)
        self.assertEqual(m.get_position(), pos)

    def testBackwardTwoRevolutions(self):
        m = Motor()
        pos = m.get_position()
        m.single_step_back(m.get_steps_per_revolution()*2)
        self.assertEqual(m.get_position(), pos)

    def testForwardHalfRevolution(self):
        m = Motor()
        pos = m.get_position()
        m.single_step(m.get_steps_per_revolution()/2)
        self.assertEqual(m.get_position(), pos+(m.get_steps_per_revolution()/2))

    def testBackwardHalfRevolution(self):
        m = Motor()
        pos = m.get_position()
        m.single_step_back(m.get_steps_per_revolution()/2)
        self.assertEqual(m.get_position(), pos+(m.get_steps_per_revolution()/2))

