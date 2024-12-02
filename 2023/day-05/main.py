lines = open("input2.txt").readlines()

firstamount = 0
secondamount = 0

###
seeds, *blocks = open("input.txt").read().split('\n\n')
seeds = [int(numeric_string) for numeric_string in seeds.split(":")[1].split()]

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:        
        line = [int(numeric_string) for numeric_string in line.split()]
        ranges.append(line)
    new = []
    for seed in seeds:
        for destination, start, rang in ranges:
            if start < seed < start + rang:
                new.append(seed - start + destination)
                break
        else:
            new.append(seed)
    seeds = new

firstamount = min(seeds)

###
print(f'First answer: {str(firstamount)}')

###
inputs, *blocks = open("input.txt").read().split('\n\n')
inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))



for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:        
        line = [int(numeric_string) for numeric_string in line.split()]
        ranges.append(line)
    new = []
    while seeds:
        starting, ending = seeds.pop()
        for destination, start, rang in ranges:
            overlapstart = max(starting, start)
            overlapend = min(ending, start + rang)
            if(overlapstart < overlapend):
                new.append((overlapstart - start + destination, overlapend - start + destination ))
                if overlapstart > starting:
                    seeds.append((starting, overlapstart))
                if ending > overlapend:
                    seeds.append((overlapend,ending))
                break
        else:
            new.append((starting,ending))
    seeds = new
    
secondamount = min(seeds)[0]

###
print(f'Second answer: {str(secondamount)}')