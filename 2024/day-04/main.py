import os
from helpers import tsprint

data = open(0).read().splitlines()

### Solution for part one
def part_one():
  answer = 0
  for rownum,row in enumerate(data):
    for charnum,char in enumerate(row):
      if data[rownum][charnum] != 'X': continue
      for directionrow in [-1,0,1]:
        for directioncol in [-1,0,1]:
          if directionrow == directioncol == 0: continue # Skip the current position
          if not (0 <= rownum + 3 * directionrow < len(data) and 0 <= charnum + 3 * directioncol < len(data[0])): continue # Skip if out of bounds
          if data[rownum+directionrow][charnum+directioncol] == 'M' and data[rownum+2*directionrow][charnum+2*directioncol] == 'A' and data[rownum+3*directionrow][charnum+3*directioncol] == 'S':
            answer += 1
  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0
  for rownum,row in enumerate(data):
    if rownum == 0 or rownum == len(data) - 1:
        continue
    for charnum,char in enumerate(row):
      if charnum == 0 or charnum == len(data[0]) - 1:
        continue
      if data[rownum][charnum] != 'A': continue
      xcoords = data[rownum-1][charnum-1] + data[rownum-1][charnum+1] + data[rownum+1][charnum+1] + data[rownum+1][charnum-1]
      if xcoords in ["MMSS", "SSMM", "MSSM", "SMMS"]:
        answer += 1

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()