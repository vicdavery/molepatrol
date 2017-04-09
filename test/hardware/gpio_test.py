import unittest
import unittest.mock
from suite import TestSettings
from enum import Enum
from molepatrol.hardware.patroller_gpio import Patroller_GPIO, Motor_0_Pins, Motor_1_Pins

class GPIOTestCase(unittest.TestCase):
    """
    This test fixture should ensure that the gpio module is able to deal with the hardware accurately.
    In order to prove this, it is necessary to mock the hardware itself. This will allow us to provide
    responses that we would expect from the hardware in any given state.
    """
    @unittest.mock.patch('molepatrol.hardware.patroller_gpio.GPIO.Hardware')
    def test_motor0_pin_config(self, mock_class):
        g = Patroller_GPIO()
        # Firstly ensure the pins are set to the correct function.
        mock_class.pin_function.return_value = mock_class.OUT
        self.assertTrue(g.is_output(Motor_0_Pins.current))
        self.assertTrue(mock_class.pin_function.called, "Calling is_output should call pin_function")
        self.assertFalse(g.is_input(Motor_0_Pins.current))
        self.assertTrue(mock_class.pin_function.called, "Calling is_input should call pin_function")
        self.assertTrue(g.is_output(Motor_0_Pins.pwm))
        self.assertTrue(mock_class.pin_function.called, "Calling is_output should call pin_function")
        self.assertTrue(g.is_output(Motor_0_Pins.direction))
        self.assertTrue(mock_class.pin_function.called, "Calling is_output should call pin_function")

    @unittest.mock.patch('molepatrol.hardware.patroller_gpio.GPIO.Hardware')
    def test_motor1_pin_config(self, mock_class):
        g = Patroller_GPIO()
        # Firstly ensure the pins are set to the correct function.
        mock_class.pin_function.return_value = mock_class.OUT
        self.assertTrue(g.is_output(Motor_1_Pins.current))
        self.assertTrue(mock_class.pin_function.called, "Calling is_output should call pin_function")
        self.assertFalse(g.is_input(Motor_1_Pins.current))
        self.assertTrue(mock_class.pin_function.called, "Calling is_input should call pin_function")
        self.assertTrue(g.is_output(Motor_1_Pins.pwm))
        self.assertTrue(mock_class.pin_function.called, "Calling is_output should call pin_function")
        self.assertTrue(g.is_output(Motor_1_Pins.direction))
        self.assertTrue(mock_class.pin_function.called, "Calling is_output should call pin_function")


    @unittest.mock.patch('molepatrol.hardware.patroller_gpio.GPIO.Hardware')
    def test_motor0_forward(self, mock_class):
        """
        Check that when we instruct motor 0 to go fowrward the correct pins are set.
        """
        mock_class.pin_function.return_value = mock_class.OUT
        g = Patroller_GPIO()

        g.set_high(Motor_0_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_high should call output")
        g.set_high(Motor_0_Pins.direction)
        self.assertTrue(mock_class.output.called, "Calling set_high from any pin should call output")
        g.set_low(Motor_0_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_low should call output")

    @unittest.mock.patch('molepatrol.hardware.patroller_gpio.GPIO.Hardware')
    def test_motor1_forward(self, mock_class):
        mock_class.pin_function.return_value = mock_class.OUT
        g = Patroller_GPIO()

        g.set_high(Motor_1_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_high should call output")
        g.set_high(Motor_1_Pins.direction)
        self.assertTrue(mock_class.output.called, "Calling set_high from any pin should call output")
        g.set_low(Motor_1_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_low should call output")

    @unittest.mock.patch('molepatrol.hardware.patroller_gpio.GPIO.Hardware')
    def test_motor0_backward(self, mock_class):
        mock_class.pin_function.return_value = mock_class.OUT
        g = Patroller_GPIO()

        g.set_high(Motor_0_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_high should call output")
        g.set_low(Motor_0_Pins.direction)
        self.assertTrue(mock_class.output.called, "Calling set_low from any pin should call output")
        g.set_low(Motor_0_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_low should call output")

    @unittest.mock.patch('molepatrol.hardware.patroller_gpio.GPIO.Hardware')
    def test_motor1_backward(self, mock_class):
        mock_class.pin_function.return_value = mock_class.OUT
        g = Patroller_GPIO()

        g.set_high(Motor_1_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_high should call output")
        g.set_low(Motor_1_Pins.direction)
        self.assertTrue(mock_class.output.called, "Calling set_low from any pin should call output")
        g.set_low(Motor_1_Pins.current)
        self.assertTrue(mock_class.output.called, "Calling set_low should call output")

    @unittest.mock.patch('molepatrol.hardware.patroller_gpio.GPIO.Hardware')
    def test_current_sensor(self, mock_class):
        mock_class.pin_function.return_value = mock_class.IN
        g = Patroller_GPIO()


#    @unittest.mock.patch('patroller_gpio.GPIO')
#    def test_motor0_different_speeds(self, GPIO): pass
#
#    @unittest.mock.patch('patroller_gpio.GPIO')
#    def test_motor1_different_speeds(self, GPIO): pass

