
class Motor(object):
    """
    The Motor class represents a motor, and provides the interface required for driving it.
    The only abilities it has are to run the motor forward or backward. Anything more sophisticated will
    be controlled by higher level classes.
    """

    def __init__(self):
       self.forward_pin = 0
       self.backward_pin = 0

    def forward(self):
        # ****
        # Insert the hardware code here
        # ****
        #
        self.backward_pin = 0
        self.forward_pin = 1

    def backward(self):
        # ****
        # Insert the hardware code here
        # ****
        #
        self.forward_pin = 0
        self.backward_pin = 1

    def stop(self):
        # ****
        # Insert the hardware code here
        # ****
        #
        self.forward_pin = 0
        self.backward_pin = 0

