import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        loc1 = Location("Chicago", 41.9, 87.6)
        loc2 = Location("Chicago", 41.9, 87.6)
        self.assertEqual(loc1 == loc2, True)

if __name__ == "__main__":
        unittest.main()
