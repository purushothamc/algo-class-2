#!/usr/bin/python

import math

def merge_and_count_splitinv(left, right):
  if left is None: left = []
  if right is None: right = []

  i = 0
  j = 0
  splitinvs = 0
  result = []

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      splitinvs += len(left) - i
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return (result, splitinvs)

def count_and_mergesort(lst):
  if len(lst) <= 1:
    return (lst, 0)
  
  middle = len(lst) / 2
  left = lst[:middle]
  right = lst[middle:]

  (left, splitinvl) = mergesort(left)
  (right, splitinvr) = mergesort(right)

  (res, splitinvs) = merge_and_count_splitinv(left, right)
  return (res, splitinvs+splitinvl+splitinvr)

with open("IntegerArray.txt") as f:
  data = f.readlines()
  intdata = [ int(x) for x in data ]
  print count_and_mergesort(intdata)[1]
