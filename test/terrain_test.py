import unittest
from mole_patrol import TerrainDescriptor, TerrainType, Terrain, NoTileException

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
        t = Terrain(4,4)
        self.assertEqual(t.get_size(), (4,4))
        t2 = Terrain(5,6)
        self.assertEqual(t2.get_size(), (5,6))

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

    def testOutOfBoundsRequests(self):
        t = Terrain(2,2)
        self.assertRaises(t.get_tile_type(0,0), NoTileException)
        self.assertRaises(t.get_tile_type(0,3), OutOfRangeException)

if __name__ == '__main__':
    unittest.main()
