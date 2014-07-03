import unittest
import unittest.mock
import time
from motor import Motor
from suite import TestSettings
from patroller_gpio import Patroller_GPIO, Motor_0_Pins, Motor_1_Pins

class MotorTestCase(unittest.TestCase):
    """
    At this level of abstraction our sensing methods are still through the mocked GPIO hardware.
    When we run the motor then we expect the GPIO pins to be called appropriately which we will
    check using the mocked GPIO.
    """
    @unittest.mock.patch('motor.Patroller_GPIO')
    def testMotorInitialisation(self, mock_class):
        m = Motor(Motor_0_Pins)
        calls = [unittest.mock.call(Motor_0_Pins.current), unittest.mock.call(Motor_0_Pins.direction), unittest.mock.call(Motor_0_Pins.pwm)]
        m.gpio.set_low.assert_has_calls(calls)

    @unittest.mock.patch('motor.Patroller_GPIO')
    def testForward100Percent(self, mock_class):
        #mock_class.is_output.return_value = True
        m = Motor(Motor_0_Pins)

        self.assertTrue(m.gpio.set_low.called, "Expect a call to set_low")

        m.forward(100)
        m.gpio.set_high.assert_called_with(Motor_0_Pins.pwm)
        #self.assertTrue(mock_class.output.called
        #self.assertTrue(mock_class.pin_function.called, "Calling is_output should call pin_function")
        #g.set_low(Patroller_GPIO.Pins.motor_1_current)
        #self.assertTrue(mock_class.output.called, "Calling set_low should call output")
    @unittest.skip("Not implemented yet")
    def testBackward100Percent(self):
        m = Motor()
        m.backward(100)
        self.assertGreater(m.current_drain(), 0, "The current drain should not be 0 when the motor is running")

    @unittest.skip("Not implemented yet")
    def testForward50Percent(self):
        m = Motor()
        m.forward(50)
        self.assertGreater(m.current_drain(), 0, "The current drain should not be 0 when the motor is running")

    @unittest.skip("Not implemented yet")
    def testBackward50Percent(self):
        m = Motor()
        m.backward(50)
        self.assertGreater(m.current_drain(), 0, "The current drain should not be 0 when the motor is running")

    @unittest.skip("Not implemented yet")
    def testCurrentIncreaseWithHigherOutput(self):
        m = Motor()
        m.forward(20)
        drain = m.current_drain()
        self.assertGreater(drain, 0, "The current drain should not be 0 when the motor is running")
        m.forward(40)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 40% than at 20%")
        drain = m.current_drain()
        m.forward(60)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 60% than at 40%")
        drain = m.current_drain()
        m.forward(80)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 80% than at 60%")
        drain = m.current_drain()
        m.forward(100)
        self.assertGreater(m.current_drain(), drain, "The current drain should be greater at 100% than at 80%")
        m.stop()

