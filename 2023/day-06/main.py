lines = open("input.txt").readlines()

firstamount = 1
secondamount = 1

###
race_duration = [int(numeric_string) for numeric_string in lines[0].split()[1:]]
race_record = [int(numeric_string) for numeric_string in lines[1].split()[1:]]
for (duration, record) in zip(race_duration, race_record):
    waystowin = 0
    for charge_time in range(duration):
        distance = charge_time * duration - charge_time ** 2
        if distance > record:
            waystowin += 1
    firstamount *= waystowin

###
print(f'First answer: {str(firstamount)}')

###
race_duration = [int(numeric_string) for numeric_string in lines[0].split()[1:]]
race_duration = int(''.join(str(v) for v in race_duration))
race_record = [int(numeric_string) for numeric_string in lines[1].split()[1:]]
race_record = int(''.join(str(v) for v in race_record))
waystowin = 0
for charge_time in range(race_duration):
    distance = charge_time * race_duration - charge_time ** 2
    if distance > race_record:
        waystowin += 1
secondamount *= waystowin

###
print(f'Second answer: {str(secondamount)}')