import time
import os

lines = open("input.txt").read().splitlines()

### Function to print timestamped messages
startingtime = time.time()
def tsprint(message):
    timestamp = time.time()-startingtime
    print(f"[{timestamp:.4f}] {message}")

### Solution for part one
def part_one():
  answer = 0

  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()