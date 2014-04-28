import unittest
from discovery import PositionScan

class DiscoveryTestCase(unittest.TestCase):
    """
    The discovery process is designed to observe and classify the surrounding terrain.
    """
    def testScanAhead(self):
        """
        Ensure that we can scan immediately ahead and determine the make up.
        """
        None
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

