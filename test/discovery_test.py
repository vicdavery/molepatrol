import unittest
import unittest.mock
from discovery import PositionScanner
from terrain import TerrainType
from suite import TestSettings

@unittest.skipUnless(TestSettings.use_mocks, reason="Discovery Test requires Mocking")
class DiscoveryTestCase(unittest.TestCase):
    """
    The discovery process is designed to observe and classify the surrounding terrain.
    """
    def testScanAheadFindGrass(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
#        cvmock = unittest.mock.Mock(spec=cvCaptureFromCAM, side_effect=[True])
        p = PositionScanner()
#        img = p.capture_image()
#        self.assertEqual(TerrainType.Grass, p.classify_image(img))
#
        self.assertEqual(TerrainType.Grass, unittest.mock.Mock(spec=p.scan, side_effect=[TerrainType.Grass])(), msg="Should find Grass")

    def testScanAheadFindMolehill(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
        p = PositionScanner()
        self.assertEqual(TerrainType.Molehill, unittest.mock.Mock(spec=p.scan, side_effect=[TerrainType.Molehill])(), msg="Should find a Molehill")

    def testScanAheadFindTree(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
        p = PositionScanner()
        self.assertEqual(TerrainType.Tree,  unittest.mock.Mock(spec=p.scan, side_effect=[TerrainType.Tree])(), msg="Should find a Tree")

    def testScanAheadFindPond(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
        p = PositionScanner()
        self.assertEqual(TerrainType.Pond, unittest.mock.Mock(spec=p.scan, side_effect=[TerrainType.Pond])(), msg="Should find a Pond")

    def testScanAheadFindPaving(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
        p = PositionScanner()
        self.assertEqual(TerrainType.Paving, unittest.mock.Mock(spec=p.scan, side_effect=[TerrainType.Paving])(), msg="Should find Paving")

    def testScanAheadFindFlowerbed(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
        p = PositionScanner()
        self.assertEqual(TerrainType.Flowerbed, unittest.mock.Mock(spec=p.scan, side_effect=[TerrainType.Flowerbed])(), msg="Should find a Flowerbed")

    def testScanAheadFindFence(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
        p = PositionScanner()
        self.assertEqual(TerrainType.Fence, unittest.mock.Mock(spec=p.scan, side_effect=[TerrainType.Fence])(), msg="Should find a fence)")

    def testSpin30AndScan(self):
        """
        Ensure that we can spin 30 degrees and scan again
        """
        None
    def testStitchingScan(self):
        """
        Ensure that when we scan, spin, scan we can stitch together the images or the terrain description.
        """
        None
    def testFullSpinScan(self):
        """
        Ensure that we can do a complete 360 degree spin and scan all of our surroundings.
        """
        None
    def testDepthScan(self):
        """
        Determine how far away an obstacle is
        """
        None
    def testFullMatrixPopulationScan(self):
        """
        Ensures that eventually the complete matrix of terrain will be discovered and categorised.
        """
        None

