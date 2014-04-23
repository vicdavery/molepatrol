import unittest
from drive_system import DriveSystem

class DriveSystemTestCase(unittest.TestCase):
    def testTwoMotorDriveSystemCreation(self):
        d = DriveSystem(2)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)
        self.assertEqual(d.get_motor_status(DriveSystem.LEFT), DriveSystem.READY)
        self.assertEqual(d.get_motor_status(DriveSystem.RIGHT), DriveSystem.READY)
        self.assertEqual(d.get_motor_status(DriveSystem.FRONT_LEFT), DriveSystem.NOT_PRESENT)
        self.assertEqual(d.get_motor_status(DriveSystem.FRONT_RIGHT), DriveSystem.NOT_PRESENT)
        self.assertEqual(d.get_motor_status(DriveSystem.REAR_RIGHT), DriveSystem.NOT_PRESENT)
        self.assertEqual(d.get_motor_status(DriveSystem.REAR_LEFT), DriveSystem.NOT_PRESENT)

    def testFourMotorDriveSystem(self):
        d = DriveSystem(4)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)
        self.assertEqual(d.get_motor_status(DriveSystem.LEFT), DriveSystem.NOT_PRESENT)
        self.assertEqual(d.get_motor_status(DriveSystem.RIGHT), DriveSystem.NOT_PRESENT)
        self.assertEqual(d.get_motor_status(DriveSystem.FRONT_LEFT), DriveSystem.READY)
        self.assertEqual(d.get_motor_status(DriveSystem.FRONT_RIGHT), DriveSystem.READY)
        self.assertEqual(d.get_motor_status(DriveSystem.REAR_RIGHT), DriveSystem.READY)
        self.assertEqual(d.get_motor_status(DriveSystem.REAR_LEFT), DriveSystem.READY)

    def testForwardOneMetre(self):
        d = DriveSystem()
        d.forward(1)
        self.assertEqual(d.get_distance_travelled(), (1,0))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardOneMetre(self):
        d = DriveSystem()
        d.backward(1)
        self.assertEqual(d.get_distance_travelled(), (-1,0))
        self.assertEqual(d.get_bearing(), 0)

    def testForwardHalfMetre(self):
        d = DriveSystem()
        d.forward(0.5)
        self.assertEqual(d.get_distance_travelled(), (0.5,0))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardHalfMetre(self):
        d = DriveSystem()
        d.backward(0.5)
        self.assertEqual(d.get_distance_travelled(), (-0.5,0))
        self.assertEqual(d.get_bearing(), 0)

    def testForwardTwoMetres(self):
        d = DriveSystem()
        d.forward(2)
        self.assertEqual(d.get_distance_travelled(), (2,0))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardTwoMetres(self):
        d = DriveSystem()
        d.backward(2)
        self.assertEqual(d.get_distance_travelled(), (-2,0))
        self.assertEqual(d.get_bearing(), 0)

    def test90DegreeAntiClock(self):
        d = DriveSystem()
        d.spin(-90)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), -90)

    def test90DegreeClock(self):
        d = DriveSystem()
        d.spin(90)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test45DegreeAntiClock(self):
        d = DriveSystem()
        d.spin(-45)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test45DegreeClock(self):
        d = DriveSystem()
        d.spin(45)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test30DegreeAntiClock(self):
        d = DriveSystem()
        d.spin(-30)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test30DegreeClock(self):
        d = DriveSystem()
        d.spin(30)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)


