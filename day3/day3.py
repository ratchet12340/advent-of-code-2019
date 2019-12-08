#!/usr/bin/env python3

def read_file():
  with open("input.txt") as f:
    w1 = f.readline().strip().split(",")
    w2 = f.readline().strip().split(",")
  return w1, w2

def get_locs(path):
  locs = {}
  last_x = 0
  last_y = 0
  total_steps = 0

  for move in path:
    direction = move[0]
    steps = int(move[1:])

    if direction == "U":
      for i in range(last_y + 1, last_y + steps + 1):
        loc = (last_x, i)
        total_steps += 1
        locs[loc] = total_steps
      last_y = last_y + steps

    elif direction == "D":
      for i in range(last_y - 1, last_y - steps - 1, -1):
        loc = (last_x, i)
        total_steps += 1
        locs[loc] = total_steps
      last_y = last_y - steps

    elif direction == "L":
      for i in range(last_x - 1, last_x - steps - 1, -1):
        loc = (i, last_y)
        total_steps += 1
        locs[loc] = total_steps
      last_x = last_x - steps

    elif direction == "R":
      for i in range(last_x + 1, last_x + steps + 1):
        loc = (i, last_y)
        total_steps += 1
        locs[loc] = total_steps
      last_x = last_x + steps

  return locs

w1, w2 = read_file()
w1_locs = get_locs(w1)
w2_locs = get_locs(w2)

inters = {}
for w1_loc in w1_locs.keys():
  if w1_loc in w2_locs:
    inters[w1_loc] = w1_locs[w1_loc] + w2_locs[w1_loc]

print(inters)
print(min(inters.values()))

# FOR PART A:
# for inter in inters:
#   print(w1_locs[inter])

# dists = []
# for inter in inters:
#   dist = abs(inter[0]) + abs(inter[1])
#   dists.append(dist)
# print(min(dists))
