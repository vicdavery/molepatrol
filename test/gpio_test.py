import unittest
from suite import TestSettings
from enum import Enum
from patroller_gpio import Patroller_GPIO
import RPi.GPIO as GPIO


class GPIOTestCase(unittest.TestCase):

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor1_forward(self, GPIO):
        GPIO.pin_function.return_value = GPIO.OUT
        g = Patroller_GPIO()
        self.assertTrue(g.is_output(GPIO.Pins.motor_out_1))
        self.assertTrue(GPIO.pin_function.called, "Calling is output should call to pin_function")
        self.assertFalse(g.is_input(GPIO.Pins.motor_out_1))
        g.set_high(Patroller_GPIO.Pins.motor_out_1)


    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor2_forward(self, GPIO): pass

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor1_backward(self, GPIO): pass

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor2_backward(self, GPIO): pass

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor1_different_speeds(self, GPIO): pass

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor2_different_speeds(self, GPIO): pass

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor1_backward(self, GPIO): pass

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor1_backward(self, GPIO): pass

    @unittest.mock.patch('patroller_gpio.GPIO')
    def test_motor1_backward(self, GPIO): pass


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
        g.set_high(Patroller_GPIO.Pins.motor_out_1)
        self.assertTrue(GPIO.output.called, "Ensure that the output setter is called")
        g.set_low(Patroller_GPIO.Pins.motor_out_1)
        self.assertTrue(GPIO.output.called, "Ensure that the output setter is called")
        g.high(Patroller_GPIO.Pins.motor_out_1)
        self.assertFalse(GPIO.input.called, "This is an output pin so we shouldn't test it's value")

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
        g.set_high(Patroller_GPIO.Pins.motor_out_2)
        self.assertTrue(GPIO.output.called, "Ensure that the output setter is called")
        g.set_low(Patroller_GPIO.Pins.motor_out_2)
        self.assertTrue(GPIO.output.called, "Ensure that the output setter is called")
        g.high(Patroller_GPIO.Pins.motor_out_2)
        self.assertFalse(GPIO.input.called, "This is an output pin so we shouldn't test it's value")

    @unittest.mock.patch('patroller_gpio.GPIO')
    def testMotor1CurrentSensor(self, GPIO):
        """
        Test that the pin is an input pin and that when we run the motor
        the current sensor value changes
        """
        # Setup the mock values
        GPIO.input.return_value = False
        GPIO.pin_function.return_value = GPIO.INPUT

        g = Patroller_GPIO()
        g.is_output(Patroller_GPIO.Pins.motor_sensor_1)
        self.assertTrue(GPIO.pin_function.called, "Calling is_output should call the underlying pin_function")
        self.assertTrue(g.is_input(Patroller_GPIO.Pins.motor_sensor_1), "This pin should be an input")
        self.assertFalse(g.is_output(Patroller_GPIO.Pins.motor_sensor_1), "This pin should be an input")
        g.set_high(Patroller_GPIO.Pins.motor_sensor_1)
        self.assertFalse(GPIO.output.called, "Ensure that the output setter is not called, this is an input pin")
        g.set_low(Patroller_GPIO.Pins.motor_sensor_1)
        self.assertFalse(GPIO.output.called, "Ensure that the output setter is not called, this is an input pin")
        g.set_high(Patroller_GPIO.Pins.motor_out_1)
        GPIO.input.return_value = 10
        self.assertGreater(g.value(Patroller_GPIO.Pins.motor_sensor_1), 0, "The current sensor should increase when we run the motor")
        g.set_low(Patroller_GPIO.Pins.motor_out_1)


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
        self.assertTrue(g.is_input(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an input")
        self.assertFalse(g.is_output(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an input")

    @unittest.mock.patch('patroller_gpio.GPIO')
    def testOpticalEncoder1(self, GPIO):
        """
        When motor is not running then the encoder value should not change
        When motor is running then the encoder value should be changing
        """
        # Setup the mock values
        GPIO.input.return_value = True
        GPIO.pin_function.return_value = GPIO.INPUT

        g = Patroller_GPIO()
        g.is_output(Patroller_GPIO.Pins.motor_sensor_2)
        self.assertTrue(GPIO.pin_function.called, "Calling is_output should call the underlying pin_function")
        self.assertTrue(g.is_input(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an input")
        self.assertFalse(g.is_output(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an input")

    @unittest.mock.patch('patroller_gpio.GPIO')
    def testOpticalEncoder2(self, GPIO):
        """
        When motor is not running then the encoder value should not change
        When motor is running then the encoder value should be changing
        """
        GPIO.input.return_value = True
        GPIO.pin_function.return_value = GPIO.INPUT

        g = Patroller_GPIO()
        g.is_output(Patroller_GPIO.Pins.motor_sensor_2)
        self.assertTrue(GPIO.pin_function.called, "Calling is_output should call the underlying pin_function")
        self.assertTrue(g.is_input(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an input")
        self.assertFalse(g.is_output(Patroller_GPIO.Pins.motor_sensor_2), "This pin should be an input")


