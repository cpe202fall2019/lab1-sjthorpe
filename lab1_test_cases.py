import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """checks max_list_iter for full and empty lists, and exception"""
        tlist = None
        with self.assertRaises(ValueError):  # checks for exception
            max_list_iter(tlist)
            
        self.assertEqual(max_list_iter([1,9,3,14,6]),14) # checks that max_list_iter returns the max for a full list of values
        self.assertEqual(max_list_iter([]),None) # checks that max_list_iter returns None for an empty list


    def test_reverse_rec(self):
        """checks reverse_rec for odd and even long lists, length one list, empty list, and exception"""
        tlist = None
        with self.assertRaises(ValueError):  # checks for exception
            reverse_rec(tlist)
        
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # checks that reverse_rec reverses odd length list
        self.assertEqual(reverse_rec([1,2,3,4,5,7]),[7,5,4,3,2,1]) # checks that reverse_rec reverses even length list
        self.assertEqual(reverse_rec([7]),[7]) # checks that reverse_rec reverses list of length 1
        self.assertEqual(reverse_rec([]),[]) # checks that reverse_rec returns empty list for empty list
        


    def test_bin_search(self):
        """tests bin_search for target that does exist and does not exist, empty list, and exception"""
        tlist = None
        with self.assertRaises(ValueError):  # checks for exception
            bin_search(5, 0 , 0, tlist)
        
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4) # checks that bin_search returns correct index for target that exists in the list
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None) # checks that bin_search returns None for target that does not exist in the list

        list_val = []
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val),None) # checks that bin_search returns None for empty list


if __name__ == "__main__":
        unittest.main()
