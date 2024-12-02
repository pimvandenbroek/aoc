directions, *rest = open("input.txt").read().splitlines()

firstamount = 0
secondamount = 0

###
directions = directions.replace('L','0').replace('R','1')

start = 'AAA'
end = 'ZZZ'

options = {}
for entry in rest:
    if entry != '':
        current, destination = entry.split(" = ")
        left, right = destination.split(", ")
        options[current] = [left.replace('(',''),right.replace(')','')]

while start != end:
    firstamount += 1
    start = options[start][int(directions[0])]
    directions = directions[1:] + directions[0]

###
print(f'First answer: {str(firstamount)}')

###

###
print(f'Second answer: {str(secondamount)}')