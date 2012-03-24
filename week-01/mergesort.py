#!/usr/bin/python

import math

def merge(left, right):
  if left is None: left = []
  if right is None: right = []

  i = 0
  j = 0
  result = []

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

def mergesort(lst):
  if len(lst) <= 1:
    return lst
  
  middle = len(lst) / 2
  left = lst[:middle]
  right = lst[middle:]

  left = mergesort(left)
  right = mergesort(right)

  return merge(left, right)

a = [ 0, 6, 5, 13, 3, 1, 8, 15, 7, 2, 4, 10, 12, 9, 11 ]

print(mergesort(a))
