#!/usr/bin/env python3

from math import floor

def read_input(filename):
  with open(filename) as f:
    masses = f.readlines()
  masses = [m.strip() for m in masses]
  masses = [int(m) for m in masses]
  return masses

def calc_fuel(mass):
  return floor(mass/3.0) - 2

def calc_total_fuel(module):
  total = 0
  fuel = module
  while fuel > 0:
    fuel = calc_fuel(fuel)
    if fuel <= 0:
      return total
    total += fuel

masses = []
masses = read_input("input.txt")
fuels = list(map(calc_total_fuel, masses))
print(sum(fuels))
