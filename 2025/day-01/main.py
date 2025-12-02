import os
from helpers import tsprint


data = [int(line.strip().replace("L","-").replace("R","")) for line in open(0)]
startpoint = 50

### Solution for part one
def part_one(startpoint):
  answer = 0
  for turn in data:
    startpoint = (startpoint + turn) % 100
    if startpoint == 0: answer += 1

  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two(startpoint):
  answer = 0
  for turn in data:
    if turn < 0:
      div, mod = divmod(turn, -100)
      answer += div
      if startpoint != 0 and startpoint + mod <= 0:
        answer += 1
    else:
      div, mod = divmod(turn, 100)
      answer += div
      if startpoint + mod >= 100:
        answer += 1
    startpoint = (startpoint + turn) % 100

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one(startpoint)
part_two(startpoint)