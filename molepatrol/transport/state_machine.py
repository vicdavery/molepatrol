#    +-------------------------------------+
#    |                                     |
#    |                                     V
#  IDLE <---> PATROLLING --------> RETURNING TO BASE ---> CHARGING
#    ^        ^        ^                                     |
#    |        |        |                                     |
#    |        V        V                                     |
#    |    SCARING  SCANNING                                  |
#    |                                                       |
#    |                                                       |
#    +-------------------------------------------------------+

from molepatrol.util.patrol_exceptions import InvalidEventException

class State(object):
    IDLE = 0
    PATROLLING = 1
    RETURNING_TO_BASE = 2
    CHARGING = 3
    SCARING = 4
    SCANNING = 5

class Event(object):
    START_PATROL = 0
    ARRIVED_AT_MOLEHILL = 1
    DONE_SCARING = 2
    LOW_BATTERY = 3
    FULLY_CHARGED = 4
    ARRIVED_AT_BASE = 5
    SCANNING_TIME = 6
    DONE_SCANNING = 7
    DONE_PATROLLING = 8

class StateMachine(object):
    machine = { State.IDLE : {Event.START_PATROL : State.PATROLLING,
                              Event.LOW_BATTERY : State.RETURNING_TO_BASE},
                State.PATROLLING : {Event.ARRIVED_AT_MOLEHILL : State.SCARING,
                                    Event.SCANNING_TIME : State.SCANNING,
                                    Event.LOW_BATTERY : State.RETURNING_TO_BASE,
                                    Event.DONE_PATROLLING : State.IDLE},
               State.RETURNING_TO_BASE : {Event.ARRIVED_AT_BASE : State.CHARGING},
               State.CHARGING : {Event.FULLY_CHARGED : State.IDLE},
               State.SCARING : {Event.DONE_SCARING : State.PATROLLING,
                                Event.LOW_BATTERY : State.PATROLLING},
               State.SCANNING : {Event.DONE_SCANNING : State.PATROLLING,
                                 Event.LOW_BATTERY : State.PATROLLING}}
    def __init__(self):
        self.state = State.IDLE

    def handle_event(self, event):
        try:
            self.state = StateMachine.machine[self.state][event]
        except KeyError as e:
            raise InvalidEventException()

    def get_state(self):
        return self.state
