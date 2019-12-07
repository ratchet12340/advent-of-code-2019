#!/usr/bin/env python3

def read_program():
  with open("input.txt") as f:
    prog = f.readline().strip()
    prog = prog.split(",")
    prog = [int(x) for x in prog]
  return prog

def execute_program(mem):
  ip = 0
  while ip < len(mem):
    if mem[ip] == 1:
      mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
      ip += 4
    elif mem[ip] == 2:
      mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
      ip += 4
    elif mem[ip] == 99:
      break
  return mem

prog = read_program()

for noun in range(100):
  for verb in range(100):
    mem = list(prog)
    mem[1] = noun
    mem[2] = verb
    mem = execute_program(mem)
    if mem[0] == 19690720:
      print("noun:", noun, "verb:", verb)
      print(100 * noun + verb)
