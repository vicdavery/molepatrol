from enum import Enum
from molepatrol.transport.motor import Motor
import math


class DriveSystem(object):
    """
    The DriveSystem class brings together all the motors required to drive the patroller and provides an interface which is
    capable of instructing the patroller in real-world terms, e.g. distance to travel, direction to rotate to.
    """

    # Motor Position
    class MotorPosition(Enum):
        left = 0
        right = 1

    # Motor status
    class MotorStatus(Enum):
        ready = 1
        not_present = -1

    def __init__(self):
        """
        We initialise ourselves as being at location 0,0 and bearing 0. The number of motors is also critical
        as it determines the configuration of the patroller. It will be assumed that a 2 motor system has one
        motor on each side (i.e. left and right)
        """
        self.position = (0,0)
        self.bearing = 0
        self.motors = self.create_required_motors()
    def create_required_motors(self):
        return { DriveSystem.MotorPosition.left : Motor(), DriveSystem.MotorPosition.right : Motor() }

    def forward(self, distance):
        self.travel(distance)

    def backward(self, distance):
        self.travel(distance * -1.0)

    def travel(self, distance):
        rad = math.radians(self.bearing)
        if distance == 0:
            return
        try:
            new_x = math.sin(rad) * distance
            new_y = math.cos(rad) *  distance
            self.position = (self.position[0] + new_x, self.position[1] + new_y)
        except ValueError as e:
            print ("Rad: ", rad, "Dist: ", distance)
            raise

    def spin(self, degrees):
        # Handle negative turn angles and passing the full circle.
        self.bearing += (degrees + 360) % 360

    def get_position(self):
        return self.position

    def get_bearing(self):
        return self.bearing

    def get_motor_status(self, motor_posn):
        if motor_posn in self.motors:
            return DriveSystem.MotorStatus.ready
        else:
            return DriveSystem.MotorStatus.not_present
