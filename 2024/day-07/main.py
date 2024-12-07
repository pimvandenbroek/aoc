import os
from helpers import tsprint

data = open(0).read().splitlines()

def is_calc_possible(testvalue, numbers):
  if len(numbers) == 1: return testvalue == numbers[0]
  if testvalue % numbers[-1] == 0 and is_calc_possible(testvalue // numbers[-1], numbers[:-1]):
    return True
  if testvalue > numbers[-1] and is_calc_possible(testvalue - numbers[-1], numbers[:-1]):
    return True
  return False

### Solution for part one
def part_one():
  answer = 0
  for x in data:
    testvalue, numbers = x.split(':')
    testvalue = int(testvalue)
    numbers = [int(x) for x in numbers.split()]
    
    if is_calc_possible(testvalue, numbers):
      answer += testvalue

  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()