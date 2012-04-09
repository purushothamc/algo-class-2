#!/usr/bin/python

import math
import random
import copy

def get_random_nodes(g):
  n1 = random.choice(g.keys())
  n2 = random.choice(g[n1])

  return n1, n2

def karger(g):
  while len(g) > 2:
    n1, n2 = get_random_nodes(g)
    g[n1].extend(g[n2])

    for n in g[n2]:
      for i in range(len(g[n])):
        if g[n][i] == n2:
          g[n][i] = n1

    g[n1] = [ x for x in g[n1] if x != n1 ]
    del g[n2]

  return len(g.popitem()[1])

with open("kargerAdj.txt") as f:
  lines = f.readlines()
  graph = {}

  # messy dataset, lots of processing
  for line in lines:
    data = []
    for e in [ x.strip() for x in line.split(" ") if x != "" ]:
      if "\t" in e:
        es = [ int(i.strip()) for i in e.split("\t") if i != "" ]
        data.extend(es)
      else:
        data.append(int(e))

    graph[data[0]] = data[1:]

  size = []
  for i in range(1000):
    size.append(karger(copy.deepcopy(graph)))

  print min(size)
