import os
from helpers import tsprint
from collections import deque

data = open(0)
grid = [[int(num) for num in line.strip()] for line in data]

trailheads = [(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 0]

def get_score(grid,coords,part2):
  que = deque([(coords)])
  visited = {(coords)}
  passed = {(coords):1}
  score = 0
  while len(que) > 0:
    cur_x, cur_y = que.popleft()
    if part2:
      if grid[cur_x][cur_y] == 9:
        score += passed[(cur_x,cur_y)]  
    for next_x, next_y in [(cur_x+1,cur_y),(cur_x-1,cur_y),(cur_x,cur_y+1),(cur_x,cur_y-1)]:
      if next_x < 0 or next_y < 0 or next_x >= len(grid) or next_y >= len(grid[0]): continue
      if grid[next_x][next_y] != grid[cur_x][cur_y] + 1: continue
      if part2:
        if (next_x,next_y) in passed:
          passed[(next_x,next_y)] += passed[(cur_x,cur_y)]
          continue
        passed[(next_x,next_y)] = passed[(cur_x,cur_y)]
      else:
        if (next_x,next_y) in visited: continue
        visited.add((next_x,next_y))
        if grid[next_x][next_y] == 9:
          score += 1
          continue
      que.append((next_x,next_y))
  return score


### Solution for part one
def part_one():
  answer = 0
  answer = sum(get_score(grid,coords, False) for coords in trailheads)
    
  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0
  answer = sum(get_score(grid,coords, True) for coords in trailheads)
  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()