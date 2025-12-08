import os
import re, math
from helpers import tsprint, ttime

data = open(0).read().splitlines()


### Solution for part one
def part_one():
  answer = 0
  grid = [re.split(r"\s+", line.strip()) for line in data]
  newgrid = []
  for col in range(len(grid[0])):
    newrow = []
    for row in range(len(grid)):
      newrow.append(grid[row][col])
    newgrid.append(newrow)
  grid = newgrid

  for problem in grid:
    operator = problem[-1]
    solution = 1 if operator == "*" else 0
    for value in problem[:-1]:
      if operator == "*":
        solution *= int(value)
      else:
        solution += int(value)
    answer += solution

  tsprint(f"First answer: {str(answer)}")
  return ttime()


### Solution for part two
def part_two():
  answer = 0
  # Split on one or more whitespaces

  operators = data.pop().split()
  rows = range(len(data))
  columns = range(len(data[0]))
  problemcunt = 0
  newproblems = []

  for column in columns:
    newval = ""
    for row in rows:
      newval += data[row][column]
    if newval.strip() != "":
      newproblems.append(int(newval.strip()))
    if newval.strip() == "":
      newproblems.append(operators.pop(0))
  newproblems.append(operators.pop(0))

  newarray = []
  while len(newproblems) > 0:
    value = newproblems.pop(0)
    if value in ("*", "+"):
      if value == "+":
        answer += sum(newarray)
      else:
        answer += math.prod(newarray)
      newarray = []
    else:
      newarray.append(value)

  tsprint(f"Second answer: {str(answer)}")
  return ttime()


### Running the solutions
tsprint(f"Starting {os.path.basename(os.getcwd())}")
part_one_time = part_one()
part_two_time = part_two()
tsprint(
  f"Part two took {round(part_two_time / part_one_time, 2)} times longer than part one"
)
tsprint(f"Finished {os.path.basename(os.getcwd())}")
