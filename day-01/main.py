import re

total = 0
with open('input.txt') as f:
   for line in f:
        numbers = re.findall(r'\d+', line)
        numberlist = ''.join(numbers)
        concat = f'{numberlist[0]}{numberlist[-1]}'
        total += int(concat)

print(f'First answer: {str(total)}')


total = 0
with open('input.txt') as f:
    for line in f:
        line = line.replace("one", "one1one")
        line = line.replace("two", "two2two")
        line = line.replace("three", "three3three")
        line = line.replace("four", "four4four")
        line = line.replace("five", "five5five")
        line = line.replace("six", "six6six")
        line = line.replace("seven", "seven7seven")
        line = line.replace("eight", "eight8eight")
        line = line.replace("nine", "nine9nine")
        print(line)
        numbers = re.findall(r'\d+', line)
        numberlist = ''.join(numbers)
        concat = f'{numberlist[0]}{numberlist[-1]}'
        print(concat)
        total += int(concat)

print(f'Second answer: {str(total)}')