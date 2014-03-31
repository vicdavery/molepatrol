
class State(object):
    IDLE = 0
    PATROLLING = 1
    CHARGING = 2
    SCARING = 3
    SCANNING = 4

class Event(object):
    START_PATROL = 0

class StateMachine(object):
    machine = { State.IDLE : {Event.START_PATROL : State.PATROLLING} }
    def __init__(self):
        self.state = State.IDLE

    def handle_event(self, event):
        self.state = StateMachine.machine[self.state][event]

    def get_state(self):
        return self.state
