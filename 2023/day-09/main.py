from itertools import pairwise

lines = open("input.txt").readlines()

firstamount = 0
secondamount = 0

###
def diffchecker(inputarray):
    if set(inputarray) == {0}:
        return 0

    next_row = [b - a for a, b in pairwise(inputarray)]
    result = diffchecker(next_row)

    return inputarray[-1] + result
        
for line in lines:
    orig_values = [int(val) for val in line.split()]
    firstamount += diffchecker(orig_values)

###
print(f'First answer: {str(firstamount)}')

###
def diffchecker(inputarray):
    if set(inputarray) == {0}:
        return 0

    next_row = [b - a for a, b in pairwise(inputarray)]
    result = diffchecker(next_row)

    return inputarray[0] - result
        
for line in lines:
    orig_values = [int(val) for val in line.split()]
    secondamount += diffchecker(orig_values)

###
print(f'Second answer: {str(secondamount)}')