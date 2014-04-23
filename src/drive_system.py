from motor import Motor


class DriveSystem(object):
    """
    The DriveSystem class brings together all the motors required to drive the patroller and provides an interface which is 
    capable of instructing the patroller in real-world terms, e.g. distance to travel, direction to rotate to.
    """
    LEFT = 0
    RIGHT = 1
    FRONT_LEFT = 2
    FRONT_RIGHT = 3
    REAR_LEFT = 4
    REAR_RIGHT = 5

    def __init__(self, num_motors):
        """
        We initialise ourselves as being at location 0,0 and bearing 0. The number of motors is also critical
        as it determines the configuration of the patroller. It will be assumed that a 2 motor system has one
        motor on each side (i.e. left and right), a 4 motor system will have front left, front rear, right front, right rear.
        """
        self.position = (0,0)
        self.bearing = 0
        self.motors

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


