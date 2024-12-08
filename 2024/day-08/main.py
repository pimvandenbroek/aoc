import os
from helpers import tsprint
import pprint

data = open(0).read().splitlines()
grid = [line for line in data]

antinodes = set()
### Solution for part one
def part_one():
  answer = 0

  antennas = {}
  for rownum, row in enumerate(grid):
    for charnum, char in enumerate(row):
      if char != '.':
        if char not in antennas:
          antennas[char] = []
        antennas[char].append((rownum, charnum))
  #print(antennas)
  for antennalist in antennas.values():
    for row in range(len(antennalist)):
      for col in range(row+1, len(antennalist)):
        row_1, col_1 = antennalist[row]
        row_2, col_2 = antennalist[col]
        if (len(grid) > 2 * row_1-row_2 >= 0) and (0 <= 2 * col_1-col_2 < len(grid[0])):
          antinodes.add((2 * row_1-row_2, 2 * col_1-col_2))
        if (len(grid) > 2 * row_2-row_1 >= 0) and (0 <= 2 * col_2-col_1 < len(grid[0])):
          antinodes.add((2 * row_2-row_1, 2 * col_2-col_1))
  answer = len(antinodes)
  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()