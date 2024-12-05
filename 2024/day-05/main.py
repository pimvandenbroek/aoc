import os
from helpers import tsprint

data = open(0).read().strip()
ordering,updates = data.split("\n\n")
ordering=[list(map(int, x.split("|"))) for x in ordering.splitlines()]
updates=[list(map(int, x.split(","))) for x in updates.splitlines()]
validate={}
for left,right in ordering:
  validate[left,right]=True
  validate[right,left]=False

def is_valid(update):
  for x in range(len(update)):
    for y in range(x+1,len(update)):
      if not validate[update[x],update[y]]:
        return False
  return True

def fix_invalid(update):
  for x in range(len(update)):
    for y in range(x+1,len(update)):
      if not validate[update[x],update[y]]:
        update[x],update[y]=update[y],update[x]
        if is_valid(update):
          return update
        fix_invalid(update)
  return update

### Solution for part one
def part_one():
  answer = 0
  for update in updates:
    if is_valid(update):
      answer+= update[len(update)//2]
  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0
  for update in updates:
    if not is_valid(update):
      new_update = fix_invalid(update)
      answer+= update[len(new_update)//2]
  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()