#!/usr/bin/python

import math
import sys

# we <3 recursion
sys.setrecursionlimit(3000000)

def dfs(g, i):
  global t
  explored[i] = True
  leader[i] = s
  for j in g[i]:
    if not explored[j]:
      dfs(g, j)

  t += 1
  finishing_time[i] = t

def dfs_loop(g):
  global s
  i = len(g)
  while (i > 0):
    if not explored[i]:
      s = i
      dfs(g, i)
    i -= 1

def reset_globals(g):
  for i in range(1, len(g)+1):
    explored[i] = False
    leader[i] = 0

# the globals we'll need to calculate the SCCs
t = 0
s = 0
explored = {}
finishing_time = {}
leader = {}

with open("SCC.txt") as data:
  graph = {}
  graph_rev = {}

  for line in data.readlines():
    line = line.strip()
    s, v = [ int(x.strip()) for x in line.split(" ") ]

    if not graph.has_key(s): graph[s] = []
    if not graph.has_key(v): graph[v] = []
    if not graph_rev.has_key(v): graph_rev[v] = []
    if not graph_rev.has_key(s): graph_rev[s] = []

    graph[s].append(v)
    graph_rev[v].append(s)

  # run the first dfs_loop to calculate the finishing times
  reset_globals(graph_rev)
  dfs_loop(graph_rev)

  # create a new graph by renaming the vertices by their finishing times
  # N.B. we're using the "graph" dictionary, *not* the graph_rev dictionary!
  graph2 = {}
  for i in range(1, len(graph)+1):
    graph2[finishing_time[i]] = [ finishing_time[x] for x in graph[i] ]
  
  # run the second dfs_loop to calculate leaders
  reset_globals(graph)
  dfs_loop(graph2)

  # which leader has the most "followers"?
  leaders = leader.values()
  top_list = dict((k, 0) for k in set(leaders))

  for leader in leaders:
    top_list[leader] += 1

  # sort the top list by dictionary value
  top_list = sorted(top_list.items(), key=lambda x: x[1], reverse=True)
  # top_list is now a list of (key,value)-pair tuples.
  # the assignment was to find the sizes of 5 largest SCCs.
  # the size of the SCC is the value of the key-value pair.
  print [ v for (k,v) in top_list[:5] ]
