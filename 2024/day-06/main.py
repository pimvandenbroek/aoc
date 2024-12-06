import os
import pprint
from helpers import tsprint

data = open(0).read().splitlines()
grid = [*map(list, data)]
direction = '^'

def find_character(grid, target):
    for row_id, row in enumerate(grid):
        for col_id, char in enumerate(row):
            if char == target:
                return (row_id, col_id)  # Return the position as (row, column)
    return None

### Solution for part one
### Highly inefficient, but it works great and fast, doesn't work with part 2, but wanted to leave it in here :)
def part_one():
  def dir_switcher(guard):
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}.get(guard)

  answer = 0
  direction = '^' #initial starting direction
  startpointx,startpointy = find_character(grid, direction)
  visited = {(startpointx, startpointy)}
  while True:
    if direction == '^':
      if startpointx-1 < 0:
        break
      elif grid[startpointx-1][startpointy] == '#':
        direction = dir_switcher(direction)
      else:
        visited.add((startpointx-1, startpointy))
        startpointx, startpointy = startpointx-1, startpointy
    elif direction == '>':
      if startpointy+1 >= len(grid[0]):
        break
      elif grid[startpointx][startpointy+1] == '#':
        direction = dir_switcher(direction)
      else:
        visited.add((startpointx, startpointy+1))
        startpointx, startpointy = startpointx, startpointy+1
    elif direction == 'v':
      if startpointx+1 >= len(grid):
        break
      elif grid[startpointx+1][startpointy] == '#':
        direction = dir_switcher(direction)
      else:
        visited.add((startpointx+1, startpointy))
        startpointx, startpointy = startpointx+1, startpointy
    elif direction == '<':
      if startpointy-1 < 0:
        break
      elif grid[startpointx][startpointy-1] == '#':
        direction = dir_switcher(direction)
      else:
        visited.add((startpointx, startpointy-1))
        startpointx, startpointy = startpointx, startpointy-1
  answer=len(visited)
  tsprint(f'First answer: {str(answer)}')

def part_one_two():
  answer = 0
  dir_x = -1
  dir_y = 0
  startpointx,startpointy=find_character(grid, direction)
  visited = set()
  while True:
    visited.add((startpointx, startpointy))
    # Check if out of bounds
    if startpointx + dir_x < 0 or startpointx + dir_x >= len(grid) or startpointy + dir_y < 0 or startpointy + dir_y >= len(grid[0]): break
    # Check if obstruction
    if grid[startpointx + dir_x][startpointy + dir_y] == '#':
        dir_x, dir_y = dir_y, -dir_x
    else:
        startpointx += dir_x
        startpointy += dir_y
  answer=len(visited)
  tsprint(f'Second First answer: {str(answer)}')


### Solution for part two
def loop_checker(grid, startpointx, startpointy):
  dir_x = -1
  dir_y = 0
  visited = set()
  while True:
    visited.add((startpointx, startpointy, dir_x, dir_y))
    # Check if out of bounds
    if startpointx + dir_x < 0 or startpointx + dir_x >= len(grid) or startpointy + dir_y < 0 or startpointy + dir_y >= len(grid[0]): return False
    # Check if obstruction
    if grid[startpointx + dir_x][startpointy + dir_y] == '#':
        dir_x, dir_y = dir_y, -dir_x
    else:
        startpointx += dir_x
        startpointy += dir_y
    if (startpointx, startpointy, dir_x, dir_y) in visited: return True

def part_two():
  answer = 0
  startpointx,startpointy=find_character(grid, '^')
  for row in range(len(grid)):
     for col in range(len(grid[0])):
        if grid[row][col] != '.':
          continue
        grid[row][col] = '#'
        if loop_checker(grid, startpointx, startpointy):
          answer += 1
        grid[row][col] = '.'
  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_one_two()
part_two()