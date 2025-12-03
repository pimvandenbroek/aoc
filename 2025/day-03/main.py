import os
from helpers import tsprint
from itertools import combinations

data = open(0).read().splitlines()


### Solution for part one
def part_one():
  answer = 0
  for x in data:
    combs = combinations(x, 2)
    currentcombo = 0
    for combination in tuple(combs):
      # convert combination from ('1', '2') to 12
      combination = int("".join(combination))
      if combination > currentcombo:
        currentcombo = combination
    answer += currentcombo

  tsprint(f"First answer: {str(answer)}")


### Solution for part two
def part_two():
  keep = 12
  answer = 0

  for line in data:
    stack = []
    to_remove = len(line) - keep
    for digit in line:
      while to_remove > 0 and stack and stack[-1] < digit:
        stack.pop()
        to_remove -= 1
      stack.append(digit)
    answer += int(''.join(stack[:keep]))
  tsprint(f"Second answer: {str(answer)}")


### Running the solutions
tsprint(f"Starting {os.path.basename(os.getcwd())}")
part_one()
part_two()
