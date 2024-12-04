import os
from helpers import tsprint

data = open(0).read().splitlines()

### Solution for part one
def part_one():
  answer = 0

  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()