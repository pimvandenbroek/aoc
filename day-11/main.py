lines = open("input2.txt").read().splitlines()

firstamount = 0
secondamount = 0

###
# zip(*lines) converts rows to columns
empty_rows = [count for count,line in enumerate(lines) if set(line) == {'.'}]
empty_cols = [count for count, line in enumerate(zip(*lines)) if set(line) == {'.'}]

for i,x in enumerate(zip(*lines)):
    print(i, x)

print(empty_cols)
###
print(f'First answer: {str(firstamount)}')

###

###
print(f'Second answer: {str(secondamount)}')