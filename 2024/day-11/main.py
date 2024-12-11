import os
from helpers import tsprint
from functools import cache

data = open(0).read()
data = [int(x) for x in data.split(" ")]

def blink(array):
  new_array = []
  for idx, stone in enumerate(array):
    if stone == 0:
      new_array.append(1)
    elif len(str(stone)) % 2 == 0 :
      split = len(str(stone)) // 2
      left, right = str(stone)[:split], str(stone)[split:]
      new_array.append(int(left))
      new_array.append(int(right))
    else:
      new_array.append(stone*2024)
  return new_array

@cache
def blink_with_cache(stone, blinks):
  if blinks == 0:
    return 1
  if stone == 0:
    return blink_with_cache(1, blinks-1)
  if len(str(stone)) % 2 == 0 :
    split = len(str(stone)) // 2
    left, right = str(stone)[:split], str(stone)[split:]
    return blink_with_cache(int(left), blinks-1) + blink_with_cache(int(right), blinks-1)
  return blink_with_cache(stone*2024, blinks-1)

### Solution for part one
def part_one():
  answer = 0
  x=0
  new_data = data
  while x < 25:
    new_data = blink(new_data)
    x+=1
  answer = len(new_data)
  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0
  answer = sum(blink_with_cache(stone, 75) for stone in data)    
  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()