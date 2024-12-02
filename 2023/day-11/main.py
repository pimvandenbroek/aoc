lines = open("input.txt").read().splitlines()

firstamount = 0
secondamount = 0

###
# zip(*lines) converts rows to columns
empty_rows = [count for count,line in enumerate(lines) if set(line) == {'.'}]
empty_cols = [count for count, line in enumerate(zip(*lines)) if set(line) == {'.'}]

galaxies = [(horizontal, vertical) for horizontal, row in  enumerate(lines) for vertical, ch in enumerate(row) if ch == "#"]

firstamount = 0
distance = 2

for i, (h1, v1) in enumerate(galaxies):
    for (h2, v2) in galaxies[:i]:
        for row in range(min(h1,h2),max(h1,h2)):
            firstamount += distance if row in empty_rows else 1
        for col in range(min(v1,v2), max(v1,v2)):
            firstamount += distance if col in empty_cols else 1
###
print(f'First answer: {str(firstamount)}')

###
empty_rows = [count for count,line in enumerate(lines) if set(line) == {'.'}]
empty_cols = [count for count, line in enumerate(zip(*lines)) if set(line) == {'.'}]

galaxies = [(horizontal, vertical) for horizontal, row in  enumerate(lines) for vertical, ch in enumerate(row) if ch == "#"]

secondamount = 0
distance = 1000000

for i, (h1, v1) in enumerate(galaxies):
    for (h2, v2) in galaxies[:i]:
        for row in range(min(h1,h2),max(h1,h2)):
            secondamount += distance if row in empty_rows else 1
        for col in range(min(v1,v2), max(v1,v2)):
            secondamount += distance if col in empty_cols else 1

###
print(f'Second answer: {str(secondamount)}')