class BatteryMonitor(object):
    EMPTY = 0
    FULLY_CHARGED = 100
    def __init__(self):
        self.charge = 0
    def get_drain_rate(self):
        return 5
    def get_status(self):
        return BatteryMonitor.FULLY_CHARGED

