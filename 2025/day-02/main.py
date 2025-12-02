import os
from helpers import tsprint


data = open(0).read().split(',')

### Solution for part one
def part_one():
  answer = 0
  for i in range(len(data)):
    rangestart, rangeend = data[i].split('-')
    for num in range(int(rangestart), int(rangeend)+1):
      strj = str(num)
      if len(strj) % 2 !=0:
        continue
      mid = len(strj)//2
      firsthalf = strj[:mid]
      secondhalf = strj[mid:]
      if firsthalf == secondhalf:
        answer += num

  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0
  for i in range(len(data)):
    rangestart, rangeend = data[i].split('-')
    for num in range(int(rangestart), int(rangeend)+1):
      strj = str(num)
      for factor in range(1, len(strj)):
        if len(strj) % factor == 0 and strj == strj[:factor] * (len(strj) // factor):
          answer += num
          break
  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()