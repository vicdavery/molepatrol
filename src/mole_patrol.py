class NoTileException(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__name__ = "No Tile Exception"
    def __str__(self):
        return repr("No Tile at (",self.x, ",", self.y, ")")

class OutOfRangeException(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__name__ = "Out Of Range Exception"
    def __str__(self):
        return repr("No Tile at (", self.x, ",", self.y, ")")

class Location(object):
    def __init__(self):
        self.x = 0
        self.y = 0

class Patroller(object):
    def __init__(self):
        None

class TerrainType(object):
    Unset = 0
    Grass = 1
    Molehill = 2
    Tree = 3
    Pond = 4
    Paving = 5
    Flowerbed = 6

class TerrainDescriptor(object):
    """
    Identifies the type of terrain at this location.
    """
    def __init__(self, terrain_type):
        self.terrain_type = terrain_type

    def get_type(self):
        return self.terrain_type
    def set_type(self, terrain_type):
        self.terrain_type = terrain_type
        return self

class Row(object):
    """
    A row of the terrain.
    """
    def __init__(self):
        self.positions = []

class Terrain(object):
    def __init__(self, x, y):
        # This will be a list of Row objects
        self.x = x
        self.y = y
        self.grid = []
        for i in range(self.x):
            self.grid.append([])
            for j in range(self.y):
                self.grid[i].append(TerrainDescriptor(TerrainType.Unset))

    def get_size(self):
        return (self.x,self.y)
    def set_tile(self, x, y, td):
        self.grid[x][y] = td
    def get_tile_type(self, x, y):
        try:
            t = self.grid[x][y].get_type()
            if t == TerrainType.Unset:
                raise NoTileException(x,y)
            return t
        except IndexError:
            raise OutOfRangeException(x,y)


class PatrolArea(object):
    def __init__(self):
        self.area_map = []



