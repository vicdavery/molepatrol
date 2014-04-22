import unittest
from terrain import TerrainDescriptor, TerrainType, Terrain
from patrol_exceptions import NoTileException, OutOfRangeException

class TerrainDescriptorTestCase(unittest.TestCase):
    def testCreateTypes(self):
        self.assertEqual(TerrainDescriptor(TerrainType.Grass).get_type(), TerrainType.Grass)
        self.assertEqual(TerrainDescriptor(TerrainType.Molehill).get_type(), TerrainType.Molehill)
        self.assertEqual(TerrainDescriptor(TerrainType.Flowerbed).get_type(), TerrainType.Flowerbed)
        self.assertEqual(TerrainDescriptor(TerrainType.Tree).get_type(), TerrainType.Tree)
        self.assertEqual(TerrainDescriptor(TerrainType.Paving).get_type(), TerrainType.Paving)
        self.assertEqual(TerrainDescriptor(TerrainType.Pond).get_type(), TerrainType.Pond)

    def testUpdateType(self):
        t = TerrainDescriptor(TerrainType.Grass)
        self.assertEqual(t.set_type(TerrainType.Molehill).get_type(), TerrainType.Molehill)
        self.assertEqual(t.set_type(TerrainType.Flowerbed).get_type(), TerrainType.Flowerbed)
        self.assertEqual(t.set_type(TerrainType.Tree).get_type(), TerrainType.Tree)
        self.assertEqual(t.set_type(TerrainType.Paving).get_type(), TerrainType.Paving)
        self.assertEqual(t.set_type(TerrainType.Pond).get_type(), TerrainType.Pond)

class TerrainGridTestCase(unittest.TestCase):
    def testCreateGrid(self):
        # It doesn't make sense to create an empty Terrain
        self.assertRaises(OutOfRangeException, Terrain, 0,0)
        self.assertEqual(Terrain(4,4).get_size(), (4,4))
        self.assertEqual(Terrain(5,6).get_size(), (5,6))


    def testAddDescriptors(self):
        t = Terrain(2,2)
        td = TerrainDescriptor(TerrainType.Grass)
        t.set_tile(0,0, td)
        self.assertEqual(t.get_tile_type(0,0), TerrainType.Grass)
        t.set_tile(0,1, td)
        t.set_tile(1,0, TerrainDescriptor(TerrainType.Flowerbed))
        t.set_tile(1,1, TerrainDescriptor(TerrainType.Molehill))
        self.assertEqual(t.get_tile_type(0,1), TerrainType.Grass)
        self.assertEqual(t.get_tile_type(1,0), TerrainType.Flowerbed)
        self.assertEqual(t.get_tile_type(1,1), TerrainType.Molehill)

    def testSetTileType(self):
        # Make sure we can change the type of a tile
        t = Terrain(3,2)
        for i in range(3):
            for j in range(2):
                t.set_tile(i,j, TerrainDescriptor(TerrainType.Grass))

        t.set_tile(0,0, TerrainDescriptor(TerrainType.Flowerbed))
        self.assertEqual(t.get_tile_type(0,0), TerrainType.Flowerbed)

        t.set_tile(0,1, TerrainDescriptor(TerrainType.Molehill))
        self.assertEqual(t.get_tile_type(0,1), TerrainType.Molehill)

        t.set_tile(1,0, TerrainDescriptor(TerrainType.Paving))
        self.assertEqual(t.get_tile_type(1,0), TerrainType.Paving)

        t.set_tile(1,1, TerrainDescriptor(TerrainType.Pond))
        self.assertEqual(t.get_tile_type(1,1), TerrainType.Pond)

        t.set_tile(2,0, TerrainDescriptor(TerrainType.Tree))
        self.assertEqual(t.get_tile_type(2,0), TerrainType.Tree)


    def testUnsetTiles(self):
        t = Terrain(2,2)
        self.assertRaises(NoTileException, t.get_tile_type, 0,0)
        self.assertRaises(NoTileException, t.get_tile_type, 1,1)
        self.assertRaises(NoTileException, t.get_tile_type, 0,1)
        self.assertRaises(NoTileException, t.get_tile_type, 1,0)

    def testOutOfBoundsRequests(self):
        t = Terrain(2,2)
        self.assertRaises(OutOfRangeException, t.get_tile_type, 0, 3)
        self.assertRaises(OutOfRangeException, t.get_tile_type, 3, 0)
        self.assertRaises(OutOfRangeException, t.get_tile_type, 1, 3)
        self.assertRaises(OutOfRangeException, t.get_tile_type, 3, 3)
        self.assertRaises(OutOfRangeException, t.get_tile_type, 3, 3)
        self.assertRaises(OutOfRangeException, t.get_tile_type, -1, 0)
        self.assertRaises(OutOfRangeException, t.get_tile_type, -1, -1)
        self.assertRaises(OutOfRangeException, t.get_tile_type, 0, -1)

if __name__ == '__main__':
    unittest.main()
