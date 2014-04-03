import unittest
from terrain_test import *

if __name__ == '__main__':
    ts = unittest.makeSuite(TerrainDescriptorTestCase)

    ts = unittest.TestSuite()
    t = TerrainDescriptorTestCase()
    ts.addTest(t)

    tr = unittest.TextTestResult()
    ts.run(tr)
    print (tr)
