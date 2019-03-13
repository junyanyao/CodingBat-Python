#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:45:36 2019

@author: YaoJunyan
"""

'''
count_evens

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''
def count_evens(nums):
  count =0
  for i in nums:
    if i%2==0:
      count +=1
    else:
      count =count
  return count

'''big_diff


Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8

'''
def big_diff(nums):
  smallest= min(nums)
  largest =max(nums)
  return largest- smallest


'''
centered_average


Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
'''
def centered_average(nums):
  min_value =min(nums)
  max_value= max(nums)
  return (sum(nums) -max_value- min_value)/(len(nums)-2)


'''has22

Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
'''
def has22(nums):
  l= ''.join(str(i) for i in nums)
  if '22' in l:
    return True
  else:
    return False

