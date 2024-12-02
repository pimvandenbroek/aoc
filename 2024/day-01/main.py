import time
import os

lines = open("input.txt").read().splitlines()

### Function to print timestamped messages
startingtime = time.time()
def tsprint(message):
    timestamp = time.time()-startingtime
    print(f"[{timestamp:.4f}] {message}")

### Parsing data
leftlist = []
rightlist=[]
for x in lines:
  left, right = x.split('   ')
  leftlist.append(left)
  rightlist.append(right)

### Solution for part one
def part_one():
  answer = 0
  leftsorted=sorted(leftlist)
  rightsorted=sorted(rightlist)

  for num, val in enumerate(leftsorted):
    answer += abs(int(rightsorted[num])-int(leftsorted[num]))

  tsprint(f'First answer: {str(answer)}')

### Solution for part two
def part_two():
  answer = 0
  for num in leftlist:
    occurrences = rightlist.count(num)
    answer += int(num) * occurrences

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()