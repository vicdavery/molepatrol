
class Motor(object):
    steps_per_revolution = 32

    def __init__(self):
       self.position = 0
    def get_position(self):
        return self.position
    def single_step(self, num=1):
        # Move forward the motor by the required number of steps
        # ****
        # Insert the hardware code here
        # ****
        #

        # Update the position according to the number of steps moved.
        self.position = (self.position + num) % Motor.steps_per_revolution

    def single_step_back(self,num=1):
        # Move backward the motor by the required number of steps
        # ****
        # Insert the hardware code here
        # ****
        #

        # Update the position according to the number of steps moved.
        self.position = ((self.position + Motor.steps_per_revolution) - num) % Motor.steps_per_revolution

    def get_steps_per_revolution(self):
        return Motor.steps_per_revolution


