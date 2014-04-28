import unittest
from drive_system import DriveSystem

class DriveSystemTestCase(unittest.TestCase):
    def testTwoMotorDriveSystemCreation(self):
        d = DriveSystem(2)
        self.assertEqual(d.get_position(), (0,0))
        self.assertEqual(d.get_bearing(), 0)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.left), DriveSystem.MotorStatus.ready)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.right), DriveSystem.MotorStatus.ready)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.front_left), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.front_right), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.rear_right), DriveSystem.MotorStatus.not_present)
        self.assertEqual(d.get_motor_status(DriveSystem.MotorPosition.rear_left), DriveSystem.MotorStatus.not_present)

    def testFourMotorDriveSystem(self):
        d = DriveSystem(4)
        self.assertEqual(d.get_position(), (0,0))
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
        self.assertEqual(d.get_position(), (0, 1))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardOneMetre(self):
        d = DriveSystem(2)
        d.backward(1)
        self.assertEqual(d.get_position(), (0, -1))
        self.assertEqual(d.get_bearing(), 0)

    def testForwardHalfMetre(self):
        d = DriveSystem(2)
        d.forward(0.5)
        self.assertEqual(d.get_position(), (0,0.5))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardHalfMetre(self):
        d = DriveSystem(2)
        d.backward(0.5)
        self.assertEqual(d.get_position(), (0, -0.5))
        self.assertEqual(d.get_bearing(), 0)

    def testForwardTwoMetres(self):
        d = DriveSystem(2)
        d.forward(2)
        self.assertEqual(d.get_position(), (0, 2))
        self.assertEqual(d.get_bearing(), 0)

    def testBackwardTwoMetres(self):
        d = DriveSystem(2)
        d.backward(2)
        self.assertEqual(d.get_position(), (0, -2))
        self.assertEqual(d.get_bearing(), 0)

    def test30DegreeAntiClock(self):
        d = DriveSystem(2)
        d.spin(-30)
        self.assertEqual(d.get_position(), (0,0))
        self.assertEqual(d.get_bearing(), 330)

    def test30DegreeClock(self):
        d = DriveSystem(2)
        d.spin(30)
        self.assertEqual(d.get_position(), (0,0))
        self.assertEqual(d.get_bearing(), 30)

    def test360DegreeClock(self):
        d = DriveSystem(2)
        d.spin(360)
        self.assertEqual(d.get_position(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test360DegreeAntiClock(self):
        d = DriveSystem(2)
        d.spin(-360)
        self.assertEqual(d.get_position(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test720DegreeClock(self):
        d = DriveSystem(2)
        d.spin(720)
        self.assertEqual(d.get_position(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test720DegreeAntiClock(self):
        d = DriveSystem(2)
        d.spin(-720)
        self.assertEqual(d.get_position(), (0,0))
        self.assertEqual(d.get_bearing(), 0)

    def test30DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(30)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], 2.5)
        self.assertAlmostEqual(d.get_position()[1], 4.330127)

    def test60DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(60)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], 4.330127)
        self.assertAlmostEqual(d.get_position()[1], 2.5)

    def test90DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(90)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], 5)
        self.assertAlmostEqual(d.get_position()[1], 0)

    def test120DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(120)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], 4.330127)
        self.assertAlmostEqual(d.get_position()[1], -2.5)

    def test150DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(150)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], 2.5)
        self.assertAlmostEqual(d.get_position()[1], -4.330127)

    def test180DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(180)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], 0)
        self.assertAlmostEqual(d.get_position()[1], -5)

    def test210DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(210)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], -2.5)
        self.assertAlmostEqual(d.get_position()[1], -4.330127)

    def test240DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(240)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], -4.330127)
        self.assertAlmostEqual(d.get_position()[1], -2.5)

    def test270DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(270)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], -5)
        self.assertAlmostEqual(d.get_position()[1], 0)

    def test300DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(300)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], -4.330127)
        self.assertAlmostEqual(d.get_position()[1], 2.5)

    def test330DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(330)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], -2.5)
        self.assertAlmostEqual(d.get_position()[1], 4.330127)


    def test360DegreeTravel(self):
        d = DriveSystem(2)
        d.spin(360)
        d.forward(5)
        self.assertAlmostEqual(d.get_position()[0], 0)
        self.assertAlmostEqual(d.get_position()[1], 5)

