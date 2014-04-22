import unittest
from state_machine import State, Event, StateMachine
from patrol_exceptions import InvalidEventException


class StateMachineCreationTestCase(unittest.TestCase):
    def testCreate(self):
        sm = StateMachine()
        self.assertEqual(sm.get_state(), State.IDLE, "When created should be in IDLE state.")
        self.assertNotEqual(sm.get_state(), State.PATROLLING, "Ensure that the IDLE state is not the same as the PATROLLING state")
        self.assertNotEqual(sm.get_state(), State.RETURNING_TO_BASE, "Ensure that the IDLE state is not the same as the RETURNING_TO_BASE state")
        self.assertNotEqual(sm.get_state(), State.CHARGING, "Ensure that the IDLE state is not the same as the CHARGING state")
        self.assertNotEqual(sm.get_state(), State.SCARING, "Ensure that the IDLE state is not the same as the SCARING state")
        self.assertNotEqual(sm.get_state(), State.SCANNING, "Ensure that the IDLE state is not the same as the SCANNING state")

    #
    # IDLE STATE
    #
    def testIdle_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        self.assertEqual(sm.get_state(), State.PATROLLING, "IDLE + START_PATROL -> PATROLLING is valid")

    def testIdle_ArrivedAtMolehill(self):
        sm = StateMachine()
        with self.assertRaises(InvalidEventException, msg="IDLE + ARRIVED_AT_MOLEHILL is not valid"):
            sm.handle_event(Event.ARRIVED_AT_MOLEHILL)

    def testIdle_DoneScaring(self):
        sm = StateMachine()
        with self.assertRaises(InvalidEventException, msg="IDLE + DONE_SCARING is not valid"):
            sm.handle_event(Event.DONE_SCARING)

    def testIdle_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE, "IDLE + LOW_BATTERY -> RETURNING_TO_BASE is valid")

    def testIdle_FullyCharged(self):
        sm = StateMachine()
        with self.assertRaises(InvalidEventException, msg="IDLE + FULLY_CHARGED is not valid"):
            sm.handle_event(Event.FULLY_CHARGED)

    def testIdle_ArrivedAtBase(self):
        sm = StateMachine()
        with self.assertRaises(InvalidEventException, msg = "IDLE + ARRIVED_AT_BASE is not valid"):
            sm.handle_event(Event.ARRIVED_AT_BASE)

    def testIdle_ScanningTime(self):
        sm = StateMachine()
        with self.assertRaises(InvalidEventException, msg = "IDLE + SCANNING_TIME is not valid"):
            sm.handle_event(Event.SCANNING_TIME)

    def testIdle_DoneScanning(self):
        sm = StateMachine()
        with self.assertRaises(InvalidEventException, msg = "IDLE + DONE_SCANNING is not valid"):
            sm.handle_event(Event.DONE_SCANNING)

    def testIdle_DonePatrolling(self):
        sm = StateMachine()
        with self.assertRaises(InvalidEventException, msg = "IDLE + DONE_PATROLLING is not valid"):
            sm.handle_event(Event.DONE_PATROLLING)

    #
    # PATROLLING
    #
    def testPatrolling_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        with self.assertRaises(InvalidEventException, msg = "PATROLLING + START_PATROL is not valid"):
            sm.handle_event(Event.START_PATROL)

    def testPatrolling_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertEqual(sm.get_state(), State.SCARING, "PATROLLING + ARRIVED_AT_MOLEHILL -> SCARING is valid")

    def testPatrolling_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        with self.assertRaises(InvalidEventException, msg = "PATROLLING + DONE_SCARING is not valid"):
            sm.handle_event( Event.DONE_SCARING)

    def testPatrolling_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE, "PATROLLING + LOW_BATTERY -> RETURNING_TO_BASE is valid")

    def testPatrolling_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        with self.assertRaises(InvalidEventException, msg = "PATROLLING + FULLY_CHARGED is not valid"):
            sm.handle_event(Event.FULLY_CHARGED)

    def testPatrolling_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        with self.assertRaises(InvalidEventException, msg = "PATROLLING + ARRIVED_AT_BASE is not valid"):
            sm.handle_event(Event.ARRIVED_AT_BASE)

    def testPatrolling_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertEqual(sm.get_state(), State.SCANNING, "PATROLLING + SCANNING_TIME -> SCANNING is valid")

    def testPatrolling_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        with self.assertRaises(InvalidEventException, msg = "PATROLLING + DONE_SCANNING is not valid"):
            sm.handle_event(Event.DONE_SCANNING)

    def testPatrolling_DonePatrolling(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.DONE_PATROLLING)
        self.assertEqual(sm.get_state(), State.IDLE, "PATROLLING + DONE_PATROLLING -> IDLE is valid")

    #
    # RETURNING TO BASE
    #
    def testReturningToBase_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + START_PATROL is invalid"):
            sm.handle_event(Event.START_PATROL)

    def testReturningToBase_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + LOW_BATTERY is invalid"):
            sm.handle_event(Event.ARRIVED_AT_MOLEHILL)

    def testReturningToBase_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + DONE_SCARING is invalid"):
            sm.handle_event(Event.DONE_SCARING)

    def testReturningToBase_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + LOW_BATTERY is invalid"):
            sm.handle_event(Event.LOW_BATTERY)

    def testReturningToBase_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + FULLY_CHARGED is invalid"):
            sm.handle_event(Event.FULLY_CHARGED)

    def testReturningToBase_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertEqual(sm.get_state(), State.CHARGING, "RETURNING_TO_BASE + ARRIVED_AT_BASE -> CHARGING is valid")

    def testReturningToBase_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + SCANNING_TIME is invalid"):
            sm.handle_event(Event.SCANNING_TIME)

    def testReturningToBase_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + DONE_SCANNING is invalid"):
            sm.handle_event(Event.DONE_SCANNING)

    def testReturningToBase_DonePatrolling(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + DONE_PATROLLING is invalid"):
            sm.handle_event(Event.DONE_PATROLLING)

    #
    # CHARGING
    #
    def testCharging_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "CHARGING + START_PATROL is invalid"):
            sm.handle_event(Event.START_PATROL)

    def testCharging_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + ARRIVED_AT_MOLEHILL is invalid"):
            sm.handle_event(Event.ARRIVED_AT_MOLEHILL)

    def testCharging_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + DONE_SCARING is invalid"):
            sm.handle_event(Event.DONE_SCARING)

    def testCharging_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + LOW_BATTERY is invalid"):
            sm.handle_event(Event.LOW_BATTERY)

    def testCharging_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        sm.handle_event(Event.FULLY_CHARGED)
        self.assertEqual(sm.get_state(), State.IDLE, "RETURNING_TO_BASE + FULLY_CHARGED -> IDLE is valid")

    def testCharging_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + ARRIVED_AT_BASE is invalid"):
            sm.handle_event(Event.ARRIVED_AT_BASE)

    def testCharging_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + SCANNING_TIME is invalid"):
            sm.handle_event(Event.SCANNING_TIME)

    def testCharging_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + DONE_SCANNING is invalid"):
            sm.handle_event(Event.DONE_SCANNING)

    def testCharging_DonePatrolling(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        with self.assertRaises(InvalidEventException, msg = "RETURNING_TO_BASE + DONE_PATROLLING is invalid"):
            sm.handle_event(Event.DONE_PATROLLING)

    #
    # SCARING
    #
    def testScaring_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        with self.assertRaises(InvalidEventException, msg = "SCARING + START_PATROL is invalid"):
            sm.handle_event(Event.START_PATROL)


    def testScaring_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        with self.assertRaises(InvalidEventException, msg = "SCARING + is invalid"):
            sm.handle_event(Event.ARRIVED_AT_MOLEHILL)

    def testScaring_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        sm.handle_event(Event.DONE_SCARING)
        self.assertEqual(sm.get_state(), State.PATROLLING, "SCARING + DONE_SCARING -> PATROLLING is valid")

    def testScaring_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE, "SCARING + LOW_BATTERY -> RETURNING_TO_BASE is valid")

    def testScaring_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        with self.assertRaises(InvalidEventException, msg = "SCARING + FULLY_CHARGED is invalid"):
            sm.handle_event(Event.FULLY_CHARGED)

    def testScaring_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        with self.assertRaises(InvalidEventException, msg = "SCARING + ARRIVED_AT_BASE is invalid"):
            sm.handle_event(Event.ARRIVED_AT_BASE)

    def testScaring_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        with self.assertRaises(InvalidEventException, msg = "SCARING + SCANNING_TIME is invalid"):
            sm.handle_event(Event.SCANNING_TIME)

    def testScaring_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        with self.assertRaises(InvalidEventException, msg = "SCARING + DONE_SCANNING is invalid"):
            sm.handle_event(Event.DONE_SCANNING)

    #
    # SCANNING
    #
    def testScanning_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        with self.assertRaises(InvalidEventException, msg = "SCANNING + START_PATROL is invalid"):
            sm.handle_event(Event.START_PATROL)

    def testScanning_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        with self.assertRaises(InvalidEventException, msg = "SCANNING + ARRIVED_AT_MOLEHILL is invalid"):
            sm.handle_event(Event.ARRIVED_AT_MOLEHILL)

    def testScanning_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        with self.assertRaises(InvalidEventException, msg = "SCANNING + DONE_SCARING is invalid"):
            sm.handle_event(Event.DONE_SCARING)

    def testScanning_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE, "SCANNING + LOW_BATTERY -> RETURNING_TO_BASE is valid")

    def testScanning_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        with self.assertRaises(InvalidEventException, msg = "SCANNING + FULLY_CHARGED is invalid"):
            sm.handle_event(Event.FULLY_CHARGED)

    def testScanning_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        with self.assertRaises(InvalidEventException, msg = "SCANNING + ARRIVED_AT_BASE is invalid"):
            sm.handle_event(Event.ARRIVED_AT_BASE)

    def testScanning_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        with self.assertRaises(InvalidEventException, msg = "SCANNING + SCANNING_TIME is invalid"):
            sm.handle_event(Event.SCANNING_TIME)

    def testScanning_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        sm.handle_event(Event.DONE_SCANNING)
        self.assertEqual(sm.get_state(), State.PATROLLING, "SCANNING + DONE_SCANNING is invalid")

if __name__ == '__main__':
    unittest.main()
