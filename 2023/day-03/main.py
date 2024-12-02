import re
from collections import defaultdict

regex = re.compile('\d+')
gears = defaultdict(list)

firstamount = 0
input = []
for line in open('input.txt').readlines():
  input.append(line.strip())

for vertical in range(len(input)):
    for match in re.finditer(regex, input[vertical]):
       for y in range(vertical-1, vertical+2):
            for x in range(match.start()-1, match.end()+1):
                if y >= 0 and y < len(input) and x >= 0 and x < len(input[y]):
                    if input[y][x] not in '0123456789.':
                        firstamount += int(match.group(0))
                        if input[y][x] == '*':
                            gears[ (y,x) ].append(match.group(0))

print(f'First answer: {str(firstamount)}')



secondamount = 0
for coords,gearvalues in gears.items():
  if len(gearvalues) == 2:
    secondamount += int(gearvalues[0]) * int(gearvalues[1])


print(f'Second answer: {str(secondamount)}')