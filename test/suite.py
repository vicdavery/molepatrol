import unittest
import sys
from argparse import ArgumentParser

class TestSettings(object):
    run_slow_tests = False

    def __init__(self):
        parser = ArgumentParser()
        parser.add_argument('-s', '--slow_tests', action='store_true')
        args = parser.parse_args()
        TestSettings.run_slow_tests = args.slow_tests

settings = TestSettings()
if __name__ == '__main__':
    ts = unittest.defaultTestLoader.discover(start_dir='.', pattern='*_test.py')
    unittest.TextTestRunner().run(ts)
