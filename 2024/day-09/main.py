import os
from helpers import tsprint

data = open(0).read()

### Solution for part one
def part_one():
  answer = 0
  returnmap = []
  fileid = 0
  for idx, entry in enumerate(data):
    nr = int(entry)
    if idx % 2 == 0:
      returnmap += [fileid] * nr
      fileid += 1
    else:
      returnmap += "." * nr

  emptyvals = [x for x,y in enumerate(returnmap) if y == "."]

  for x in emptyvals:
    while returnmap[-1] == ".": returnmap.pop()
    if len(returnmap) <= x: break
    returnmap[x] = returnmap.pop()

  answer =sum(idx * x for idx, x in enumerate(returnmap))
  tsprint(f'First answer: {str(answer)}')


### Solution for part two
def part_two():
  answer = 0
  files = {}
  blanks = []
  fileid = 0
  pos = 0

  for idx, char in enumerate(data):
      nr = int(char)
      if idx % 2 == 0:
          if nr == 0:
              raise ValueError("unexpected x=0 for file")
          files[fileid] = (pos, nr)
          fileid += 1
      else:
          if nr != 0:
              blanks.append((pos, nr))
      pos += nr

  while fileid > 0:
      fileid -= 1
      pos, size = files[fileid]
      for idx, (start, length) in enumerate(blanks):
          if start >= pos:
              blanks = blanks[:idx]
              break
          if size <= length:
              files[fileid] = (start, size)
              if size == length:
                  blanks.pop(idx)
              else:
                  blanks[idx] = (start + size, length - size)
              break

  for fileid, (pos, size) in files.items():
      for nr in range(pos, pos + size):
          answer += fileid * nr

  tsprint(f'Second answer: {str(answer)}')

### Running the solutions
tsprint(f'Starting {os.path.basename(os.getcwd())}')
part_one()
part_two()