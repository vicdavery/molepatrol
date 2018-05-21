from molepatrol.cv.discovery import PositionScanner

class MolePatroller(object):
    """
    At startup the patroller will scan its terrain, this process will take some time.
    The general approach taken, will be to observe its immediate surroundings, then move in
    one direction and circle round the starting point. Rather than circle I actually mean
    form a square.
    The path will look like the following (if taken in alphabetical order):

    +---+---+---+---+---+
    | X | Y | J | K | L |
    +---+---+---+---+---+
    | W | I | B | C | M |
    +---+---+---+---+---+
    | V | H | A | D | N |
    +---+---+---+---+---+
    | U | G | F | E | O |
    +---+---+---+---+---+
    | T | S | R | Q | P |
    +---+---+---+---+---+

    The complication will come when an obstacle is identified (e.g. tree, water, molehill).
    Rather than scanning the obstacle straightaway, it will be incorporated into the scan, but to
    do this we won't always be able to follow our path properly. So we'll need to setup a diversion
    around the obstacle and build it into the scan.

    Given the above terrain, which has obstacles at (C,D), T, (H,V), Y

    1) Start at A
    2) Scan B-I
    3) Identify obstacle present at (C,D)
    4) Create diversion which will run B->A->E
    5) Identify obstacle present at H
    6) Create diversion which will run G->A->I
    5) Move to B
    6) Scan J,K,C,D,A,H,I,Y
    7) Confirm obstacle at (C,D)
    8) Confirm obstacle at H
    9) New obstacle at Y
    10) Create diversion which will run X->I->J
    11) We want to move onto C, but there is a diversion in place which will send us to A
    12) A has already been scanned so we move to the next point in our diversion: E
    13) Scan D,N,O,P,Q,R,S,F,A
    14) Confirm obstacle at D
    15) Move to F
    16) Scan A,D,E,Q,R,S,G,H
    17) Confirm obstacles at D,H
    18) Move to G
    19) Scan H,A,F,R,S,T,U,V
    20) Confirm obstacle at H
    21) We want to move to H, but the diversion sends us through A to I
    22) Scan Y,J,B,A,H,V,W,X
    23) Confirm obstacle at Y
    24) Obstacle at H is extended to include V
    25) Create diversion for V which runs: U->G-A->I->W
    26) We want to move to Y but the diversion sends us to J
"""
    def __init__(self):
        self.state_machine = StateMachine()
    def run(self):
        while True:
            events = check_inputs()
            process_events(events)
    def check_inputs(self):
        return None
    def process_events(self, events):
        for e in events:
            self.state_machine.handle_event(e)

if __name__ == '__main__':
    patroller = MolePatroller()
    patroller.run()


