import unittest
from state_machine import State, Event, StateMachine, InvalidEventException


class StateMachineCreationTestCase(unittest.TestCase):
    def testCreate(self):
        sm = StateMachine()
        self.assertEqual(sm.get_state(), State.IDLE, "When created should be in IDLE state.")
        self.assertNotEqual(sm.get_state(), State.PATROLLING)
        self.assertNotEqual(sm.get_state(), State.RETURNING_TO_BASE)
        self.assertNotEqual(sm.get_state(), State.CHARGING)
        self.assertNotEqual(sm.get_state(), State.SCARING)
        self.assertNotEqual(sm.get_state(), State.SCANNING)

    #
    # IDLE STATE
    #
    def testIdle_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        self.assertEqual(sm.get_state(), State.PATROLLING)

    def testIdle_ArrivedAtMolehill(self):
        sm = StateMachine()
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_MOLEHILL)

    def testIdle_DoneScaring(self):
        sm = StateMachine()
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCARING)

    def testIdle_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE)

    def testIdle_FullyCharged(self):
        sm = StateMachine()
        self.assertRaises(InvalidEventException, sm.handle_event, Event.FULLY_CHARGED)

    def testIdle_ArrivedAtBase(self):
        sm = StateMachine()
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_BASE)

    def testIdle_ScanningTime(self):
        sm = StateMachine()
        self.assertRaises(InvalidEventException, sm.handle_event, Event.SCANNING_TIME)

    def testIdle_DoneScanning(self):
        sm = StateMachine()
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCANNING)

    def testIdle_DonePatrolling(self):
        sm = StateMachine()
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_PATROLLING)

    #
    # PATROLLING
    #
    def testPatrolling_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.START_PATROL)

    def testPatrolling_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertEqual(sm.get_state(), State.SCARING)

    def testPatrolling_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        sm.handle_event(Event.DONE_SCARING)
        self.assertEqual(sm.get_state(), State.PATROLLING)

    def testPatrolling_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE)

    def testPatrolling_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.FULLY_CHARGED)

    def testPatrolling_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_BASE)

    def testPatrolling_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertEqual(sm.get_state(), State.SCANNING)

    def testPatrolling_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCANNING)

    def testPatrolling_DonePatrolling(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.DONE_PATROLLING)
        self.assertEqual(sm.get_state(), State.IDLE)

    #
    # RETURNING TO BASE
    #
    def testReturningToBase_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.START_PATROL)

    def testReturningToBase_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_MOLEHILL)

    def testReturningToBase_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCARING)

    def testReturningToBase_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.LOW_BATTERY)

    def testReturningToBase_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.FULLY_CHARGED)

    def testReturningToBase_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertEqual(sm.get_state(), State.CHARGING)

    def testReturningToBase_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.SCANNING_TIME)

    def testReturningToBase_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCANNING)

    def testReturningToBase_DonePatrolling(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_PATROLLING)

    #
    # CHARGING
    #
    def testCharging_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.START_PATROL)

    def testCharging_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_MOLEHILL)

    def testCharging_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCARING)

    def testCharging_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.LOW_BATTERY)

    def testCharging_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        sm.handle_event(Event.FULLY_CHARGED)
        self.assertEqual(sm.get_state(), State.IDLE)

    def testCharging_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_BASE)

    def testCharging_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.SCANNING_TIME)

    def testCharging_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCANNING)

    def testCharging_DonePatrolling(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        sm.handle_event(Event.ARRIVED_AT_BASE)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_PATROLLING)

    #
    # SCARING
    #
    def testScaring_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.START_PATROL)


    def testScaring_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_MOLEHILL)

    def testScaring_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        sm.handle_event(Event.DONE_SCARING)
        self.assertEqual(sm.get_state(), State.PATROLLING)

    def testScaring_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE)

    def testScaring_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.FULLY_CHARGED)

    def testScaring_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_BASE)

    def testScaring_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.SCANNING_TIME)

    def testScaring_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.ARRIVED_AT_MOLEHILL)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCANNING)

    #
    # SCANNING
    #
    def testScanning_StartPatrol(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.START_PATROL)

    def testScanning_ArrivedAtMolehill(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_MOLEHILL)

    def testScanning_DoneScaring(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.DONE_SCARING)

    def testScanning_LowBattery(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state(), State.RETURNING_TO_BASE)

    def testScanning_FullyCharged(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.FULLY_CHARGED)

    def testScanning_ArrivedAtBase(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.ARRIVED_AT_BASE)

    def testScanning_ScanningTime(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        self.assertRaises(InvalidEventException, sm.handle_event, Event.SCANNING_TIME)

    def testScanning_DoneScanning(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        sm.handle_event(Event.SCANNING_TIME)
        sm.handle_event(Event.DONE_SCANNING)
        self.assertEqual(sm.get_state(), State.PATROLLING)

if __name__ == '__main__':
    unittest.main()
