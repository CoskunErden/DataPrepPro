import unittest

# Discover and run all tests
if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.TextTestRunner()
    testRunner.run(tests)
