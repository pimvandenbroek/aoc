import os
from helpers import tsprint

data = open("input.txt").read().splitlines()
data = [[int(n) for n in line.split(' ')] for line in data]


def is_safe(levels):
  increase = all(levels[i+1] > levels[i] for i in range(len(levels) -1))
  decrease = all(levels[i+1] < levels[i] for i in range(len(levels) -1))

  if increase:
    return all(1 <= int(levels[i+1]) - int(levels[i]) <= 3 for i in range(len(levels) -1))
  elif decrease:
    return all(1 <= int(levels[i]) - int(levels[i+1]) <= 3 for i in range(len(levels) -1))
  else:
    return False

def is_safe_dampened(levels):
  for num in range(len(levels)):
    newlevel = levels.copy()
    newlevel.pop(num)
    if is_safe(newlevel):
      return True
  return False

### Solution for part one
def part_one():
  answer = 0
  answer = sum(is_safe(report) for report in data)
  tsprint(f'First answer: {str(answer)}')

### Solution for part two
def part_two():
  answer = 0
  for report in data:
    if is_safe(report) != True:
      if is_safe_dampened(report) == True:
        answer += 1
    else:
      answer += 1
  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()