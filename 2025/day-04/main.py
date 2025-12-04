import os
from helpers import tsprint

data = open(0).read().splitlines()
grid = [line.replace("@", "1").replace(".", "0") for line in data]


### Solution for part one
def part_one():
  answer = 0
  for rownum, row in enumerate(grid):
    for charnum, char in enumerate(row):
      count = 0
      if char == "1":
        # count chars around current char, there are 8 directions, so 9 will not be a valid count, don't count the current char
        for row_offset in [-1, 0, 1]:
          for col_offset in [-1, 0, 1]:
            if row_offset == 0 and col_offset == 0:
              continue
            if (
              0 <= rownum + row_offset < len(grid)
              and 0 <= charnum + col_offset < len(grid[0])
              and grid[rownum + row_offset][charnum + col_offset] == "1"
            ):
              count += 1
        if count < 4:
          answer += 1

  tsprint(f"First answer: {str(answer)}")


### Solution for part two
def part_two():
  # do the same as above, but this time if a roll is removed, log its position for later processing. Then after counting, remove all logged rolls from the grid and count again.

  answer = 0
  removedrolls = []
  while True:
    while len(removedrolls) > 0:
      rownum, charnum = removedrolls.pop()
      grid[rownum] = grid[rownum][:charnum] + "0" + grid[rownum][charnum + 1 :]

    for rownum, row in enumerate(grid):
      for charnum, char in enumerate(row):
        count = 0
        if char == "1":
          # count chars around current char, there are 8 directions, so 9 will not be a valid count, don't count the current char
          for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
              if row_offset == 0 and col_offset == 0:
                continue
              if (
                0 <= rownum + row_offset < len(grid)
                and 0 <= charnum + col_offset < len(grid[0])
                and grid[rownum + row_offset][charnum + col_offset] == "1"
              ):
                count += 1
          if count < 4:
            answer += 1
            # log the position of the char in an array for later processing
            removedrolls.append((rownum, charnum))
    if len(removedrolls) == 0:
      break

  tsprint(f"Second answer: {str(answer)}")


### Running the solutions
tsprint(f"Starting {os.path.basename(os.getcwd())}")
part_one()
part_two()
