import os
from helpers import tsprint, ttime

data = open(0).read().splitlines()


### Solution for part one
def part_one():
  answer = 0

  tsprint(f"First answer: {str(answer)}")
  return ttime()


### Solution for part two
def part_two():
  answer = 0

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
