import os
from helpers import tsprint, ttime
from collections import deque
from functools import cache

grid = [list(line.strip()) for line in open(0)]

S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][
  0
]
beams = deque([S])
seen = {S}


def addseen(r, c):
  if (r, c) in seen:
    return
  seen.add((r, c))
  beams.append((r, c))


### Solution for part one
def part_one():
  answer = 0

  while len(beams) > 0:
    r, c = beams.popleft()
    if grid[r][c] == "." or grid[r][c] == "S":
      if r == len(grid) - 1:
        continue
      addseen(r + 1, c)
    elif grid[r][c] == "^":
      answer += 1
      addseen(r, c - 1)
      addseen(r, c + 1)

  tsprint(f"First answer: {str(answer)}")
  return ttime()


@cache
def solve(r, c):
  if r >= len(grid):
    return 1
  if grid[r][c] == "." or grid[r][c] == "S":
    return solve(r + 1, c)
  elif grid[r][c] == "^":
    return solve(r, c - 1) + solve(r, c + 1)


### Solution for part two
def part_two():
  answer = 0
  answer = solve(*S)
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
