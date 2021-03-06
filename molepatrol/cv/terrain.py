#
# The classes required for describing the terrain which is being patrolled.
#
from molepatrol.util.patrol_exceptions import OutOfRangeException, NoTileException

class TerrainType(object):
    Unset = 0
    Grass = 1
    Molehill = 2
    Tree = 3
    Pond = 4
    Paving = 5
    Flowerbed = 6
    Fence = 7

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

class Terrain(object):
    def __init__(self, x, y):
        # This will be a list of Row objects
        if x <= 0 or y <= 0: raise OutOfRangeException(x,y)
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
        if x < 0 or y < 0: raise OutOfRangeException(x,y)

        try:
            t = self.grid[x][y].get_type()
            if t == TerrainType.Unset:
                raise NoTileException(x,y)
        except IndexError:
            raise OutOfRangeException(x,y)
        return t




