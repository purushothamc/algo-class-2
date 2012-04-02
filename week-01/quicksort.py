#!/usr/bin/python

import math

def first_as_pivot(arr):
  """
  returns the first element of the array as the pivot.

  the function is completely unnecessary, but makes swapping 
  different approaches to choosing pivots in the main function
  easier.
  """
  return arr[0]

def last_as_pivot(arr):
  """
  returns the last element of the array as the pivot.

  does the job of moving the last element of the array to the
  beginning of the list.
  """
  arr[0], arr[-1] = arr[-1], arr[0]
  return arr[0]

def median_as_pivot(arr):
  """
  uses the median-of-three approach, identifying the median between
  the first, last and middle elements of the array and using it as 
  the pivot.

  the idea is to do a bit of extra work for better performance on
  sorted arrays.
  """
  middle = int(math.ceil(len(arr) / 2.))
  lst = sorted([ arr[0], arr[middle-1], arr[-1] ])
  median_idx = arr.index(lst[1])

  arr[0], arr[median_idx] = arr[median_idx], arr[0]
  return arr[0]

def count_and_quicksort(arr):
  if arr is None: arr = []
  if len(arr) < 2: return (arr, 0)

  pivot = median_as_pivot(arr)
  i = 1

  # could be solved much more elegantly using list comprehensions
  # e.g. http://en.literateprograms.org/Quicksort_%28Python%29
  # I tried to stay as close to the pseudocode from Roughgarden's
  # lectures.
  for j in range(1, len(arr)):
    if arr[j] < pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1

  # swap the pivot
  arr[0], arr[i-1] = arr[i-1], arr[0]

  # cheating: it's not exactly in-place, but we'll live
  (arr[:i-1], countl) = count_and_quicksort(arr[:i-1])
  (arr[i:], countr) = count_and_quicksort(arr[i:])

  count = len(arr) - 1 + countl + countr
  return (arr, count)

with open("QuickSort.txt") as f:
  data = f.readlines()
  intdata = [ int(x) for x in data ]
  print count_and_quicksort(intdata)[1]
