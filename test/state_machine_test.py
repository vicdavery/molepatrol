import unittest
from state_machine import State, Event, StateMachine


class StateMachineCreationTestCase(unittest.TestCase):
    def testCreate(self):
        sm = StateMachine()
        self.assertEqual(sm.get_state(), State.IDLE, "When created should be in IDLE state.")
        self.assertNotEqual(sm.get_state(), State.PATROLLING)
        self.assertNotEqual(sm.get_state(), State.CHARGING)
        self.assertNotEqual(sm.get_state(), State.SCARING)
        self.assertNotEqual(sm.get_state(), State.SCANNING)

    def testIdleToPatrolling(self):
        sm = StateMachine()
        sm.handle_event(Event.START_PATROL)
        self.assertEqual(sm.get_state(), State.PATROLLING)

    def testIdleToCharging(self):
        sm = StateMachine()
        sm.handle_event(Event.LOW_BATTERY)
        self.assertEqual(sm.get_state, State.CHARGING)

    def testIdleToScanning(self):
        None

    def testPatrollingToIdle(self):
        None
    def testPatrollingToScanning(self):
        None
    def testPatrollingToCharging(self):
        None
    def testPatrollingTo



if __name__ == '__main__':
    unittest.main()
