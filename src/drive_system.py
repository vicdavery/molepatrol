from enum import Enum
from motor import Motor


class DriveSystem(object):
    """
    The DriveSystem class brings together all the motors required to drive the patroller and provides an interface which is
    capable of instructing the patroller in real-world terms, e.g. distance to travel, direction to rotate to.
    """

    # Motor Position
    class MotorPosition(Enum):
        left = 0
        right = 1
        front_left = 2
        front_right = 3
        rear_left = 4
        rear_right = 5

    # Motor status
    class MotorStatus(Enum):
        ready = 1
        not_present = -1

    def __init__(self, num_motors):
        """
        We initialise ourselves as being at location 0,0 and bearing 0. The number of motors is also critical
        as it determines the configuration of the patroller. It will be assumed that a 2 motor system has one
        motor on each side (i.e. left and right), a 4 motor system will have front left, front rear, right front, right rear.
        """
        self.position = (0,0)
        self.bearing = 0
        self.motors = self.create_required_motors(num_motors)
    def create_required_motors(self, num_motors):
        if num_motors == 2:
            return { DriveSystem.MotorPosition.left : Motor(), DriveSystem.MotorPosition.right : Motor() }
        elif num_motors == 4:
            return {DriveSystem.MotorPosition.front_left : Motor(),
                    DriveSystem.MotorPosition.front_right : Motor(),
                    DriveSystem.MotorPosition.rear_left : Motor(),
                    DriveSystem.MotorPosition.rear_right : Motor() }
        else:
            raise IndexError()

    def forward(self, distance):
        self.travel(distance)

    def backward(self, distance):
        self.travel(distance * -1.0)

    def travel(self, distance):
        self.position = (distance + self.position[0], self.position[1])

    def spin(self, degrees):
        self.bearing += degrees
    def get_distance_travelled(self):
        return self.position

    def get_bearing(self):
        return self.bearing

    def get_motor_status(self, motor_posn):
        if motor_posn in self.motors:
            return DriveSystem.MotorStatus.ready
        else:
            return DriveSystem.MotorStatus.not_present