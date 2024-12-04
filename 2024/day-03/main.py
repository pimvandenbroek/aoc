import os
import re
from helpers import tsprint
data = open("input.txt").read()

### Solution for part one
def part_one():
  matches = re.findall(r"mul\((\d+),(\d+)\)", data)
  answer = 0
  for x,y in matches:
    answer += int(x) * int(y)
  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  matches = re.findall(r"(mul\(\d*,\d*\)|do\(\)|don't\(\))", data)
  answer = 0
  do = True
  for match in matches:
    if match == "do()":
      do = True
    elif match == "don't()":
      do = False
    if do and match.startswith("mul"):
      numbers = re.findall(r"mul\((\d+),(\d+)\)", match)
      for x,y in numbers:
        answer += int(x) * int(y)
  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()