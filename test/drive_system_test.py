import unittest
from drive_system import DriveSystem

class DriveSystemTestCase(unittest.TestCase):
    def testTwoMotorDriveSystemCreation(self):
        d = DriveSystem(2)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.left), DriveSystem.MotorStatus.ready)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.right), DriveSystem.MotorStatus.ready)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.front_left), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.front_right), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.rear_right), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.rear_left), DriveSystem.MotorStatus.not_present)

    def testFourMotorDriveSystem(self):
        d = DriveSystem(4)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.left), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.right), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.front_left), DriveSystem.MotorStatus.ready)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.front_right), DriveSystem.MotorStatus.ready)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.rear_right), DriveSystem.MotorStatus.ready)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.rear_left), DriveSystem.MotorStatus.ready)

    def testBadCreationOfDriveSystem(self):
        for num in [-1, 0, 1, 3, 5, 12]:
            with self.assertRaises(IndexError):
                d = DriveSystem(num)

    def testForwardOneMetre(self):
        d = DriveSystem(2)
        d.forward(1)
        self.assertEqual(d.get_distance_travelled(), (1,0))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardOneMetre(self):
        d = DriveSystem(2)
        d.backward(1)
        self.assertEqual(d.get_distance_travelled(), (-1,0))
        self.assertEqual(d.get_bearing(), 0)

    def testForwardHalfMetre(self):
        d = DriveSystem(2)
        d.forward(0.5)
        self.assertEqual(d.get_distance_travelled(), (0.5,0))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardHalfMetre(self):
        d = DriveSystem(2)
        d.backward(0.5)
        self.assertEqual(d.get_distance_travelled(), (-0.5,0))
        self.assertEqual(d.get_bearing(), 0)

    def testForwardTwoMetres(self):
        d = DriveSystem(2)
        d.forward(2)
        self.assertEqual(d.get_distance_travelled(), (2,0))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardTwoMetres(self):
        d = DriveSystem(2)
        d.backward(2)
        self.assertEqual(d.get_distance_travelled(), (-2,0))
        self.assertEqual(d.get_bearing(), 0)

    def test30DegreeAntiClock(self):
        d = DriveSystem(2)
        d.spin(-30)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test30DegreeClock(self):
        d = DriveSystem(2)
        d.spin(30)
        self.assertEqual(d.get_distance_travelled(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test30DegreeTravel(self):
        None

    def test60DegreeTravel(self):
        None

    def test90DegreeTravel(self):
        None

    def test120DegreeTravel(self):
        None

    def test150DegreeTravel(self):
        None

    def test180DegreeTravel(self):
        None

    def test210DegreeTravel(self):
        None

    def test240DegreeTravel(self):
        None

    def test270DegreeTravel(self):
        None

    def test300DegreeTravel(self):
        None

    def test330DegreeTravel(self):
        None

    def test360DegreeTravel(self):
        None

