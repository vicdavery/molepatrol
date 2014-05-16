import unittest
from suite import TestSettings
from enum import Enum
from patroller_gpio import Patroller_GPIO
import RPi.GPIO as GPIO

def mock_outputs():
    return False

class GPIOTestCase(unittest.TestCase):

    @unittest.mock.patch('patroller_gpio.GPIO')
    def testMotor1Output(self, GPIO):
        """
        Test that the pin is an output pin and that we can set it both
        high and low
        """
        GPIO.input.return_value = False
        GPIO.pin_function.return_value = GPIO.OUTPUT
        g = Patroller_GPIO()
        g.is_output(Patroller_GPIO.Pins.motor_out_1)
        self.assertTrue(GPIO.pin_function.called, "Checking input should call pin_function")
        self.assertEqual(g.is_input(Patroller_GPIO.Pins.motor_out_1), False, "This pin should be an output")
        self.assertEqual(g.is_output(Patroller_GPIO.Pins.motor_out_1), True, "This pin should be an output")

    @unittest.mock.patch('patroller_gpio.GPIO')
    def testMotor2Output(self, GPIO):
        """
        Test that the pin is an output pin and that we can set it both
        high and low
        """
        # Setup the mock values
        GPIO.input.return_value = False
        GPIO.pin_function.return_value = GPIO.OUTPUT

        g = Patroller_GPIO()
        g.is_output(Patroller_GPIO.Pins.motor_out_2)
        self.assertTrue(GPIO.pin_function.called, "Calling is_output should call the underlying pin_function")
        self.assertFalse(g.is_input(Patroller_GPIO.Pins.motor_out_2), "This pin should be an output")
        self.assertTrue(g.is_output(Patroller_GPIO.Pins.motor_out_2), "This pin should be an output")

    @unittest.mock.patch('patroller_gpio.GPIO')
    def testMotor1CurrentSensor(self, GPIO):
        """
        Test that the pin is an input pin and that when we run the motor
        the current sensor value changes
        """
        # Setup the mock values
        GPIO.input.return_value = True
        GPIO.pin_function.return_value = GPIO.INPUT

        g = Patroller_GPIO()
        g.is_output(Patroller_GPIO.Pins.motor_sensor_1)
        self.assertTrue(GPIO.pin_function.called, "Calling is_output should call the underlying pin_function")
        self.assertTrue(g.is_input(Patroller_GPIO.Pins.motor_sensor_1), "This pin should be an output")
        self.assertFalse(g.is_output(Patroller_GPIO.Pins.motor_sensor_1), "This pin should be an output")

    @unittest.mock.patch('patroller_gpio.GPIO')
    def testMotor2CurrentSensor(self, GPIO):
        """
        Test that the pin is an input pin and that when we run the motor
        the current sensor value changes
        """
        # Setup the mock values
        GPIO.input.return_value = True
        GPIO.pin_function.return_value = GPIO.INPUT

        g = Patroller_GPIO()
        g.is_output(Patroller_GPIO.Pins.motor_sensor_2)
        self.assertTrue(GPIO.pin_function.called, "Calling is_output should call the underlying pin_function")
        self.assertTrue(g.is_input(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an output")
        self.assertFalse(g.is_output(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an output")

    def testOpticalEncoder1(self):
        """
        When motor is not running then the encoder value should not change
        When motor is running then the encoder value should be changing
        """
        g = Patroller_GPIO()

    def testOpticalEncoder2(self):
        """
        When motor is not running then the encoder value should not change
        When motor is running then the encoder value should be changing
        """
        g = Patroller_GPIO()


