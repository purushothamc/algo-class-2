#!/usr/bin/python

with open("HashInt.txt") as f:
  data = f.readlines()
  intlist = [ int(x) for x in data ]
  intdict = dict((int(x), None) for x in data)

  for i in [ 231552,234756,596873,648219,726312,981237,988331,1277361,1283379 ]:
    has_key = False
    for j in intlist:
      if intdict.has_key(i-j):
        has_key = True
        break
    print (i, has_key)
