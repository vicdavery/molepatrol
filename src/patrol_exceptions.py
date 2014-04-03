#
# A file containing all exceptions used in the patroller.
#
class NoTileException(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__name__ = "No Tile Exception"
    def __str__(self):
        return repr("No Tile at ( %s, %s )" % (self.x, self.y))

class OutOfRangeException(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__name__ = "Out Of Range Exception"
    def __str__(self):
        return repr("The location (%s,%s) is not in the terrain" % (self.x, self.y))

class InvalidEventException(Exception):
    def __init__(self):
        self.__name__ = "Invalid Event Exception"
    def __str__(self):
        return repr("Cannot handle this event at the moment")

