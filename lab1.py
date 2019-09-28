import math


def max_list_iter(int_list):
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if not int_list:
      return None
   m = int_list[0]
   for i in range(len(int_list)-1):
      if int_list[i] > m:
         m = int_list[i]
   return m

def reverse_rec(int_list, i = 0):
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if not int_list:
      return int_list
   if i == (len(int_list)//2):
      return int_list
   temp = int_list[i]
   int_list[i] = int_list[len(int_list)-1-i]
   int_list[len(int_list)-1-i] = temp
   return reverse_rec(int_list, i + 1)

def bin_search(target, low, high, int_list):
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if not int_list:
      return None
   if int_list[(high+low)//2] == target:
      return (high+low)//2
   elif high == low or high-1 == low:
      if int_list[high] == target:
         return target
      return None
   elif int_list[(high+low)//2] > target:
      return bin_search(target, low, (high+low)//2, int_list)
   else:
      return bin_search(target, (high+low)//2, high, int_list)
