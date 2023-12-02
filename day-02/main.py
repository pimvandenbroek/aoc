import numpy

max = {
    'red': 12,
    'green': 13,
    'blue': 14
}
firstamount = 0

for line in open('input.txt').readlines():
    line = line.strip()
    possible = True        
    game, hands = line.split(': ')
    gamenumber = game.split(' ')[-1]
    for hand in hands.split('; '):
        for ball in hand.split(', '):
            count, color = ball.split(' ')
            if int(count) > max[color]:
                #print(f'{gamenumber} - {color} - {count}')
                possible = False
    if possible:
        firstamount += int(gamenumber)
    
print(f'First answer: {str(firstamount)}')


secondamount = 0

for line in open('input.txt').readlines():
    line = line.strip()   
    game, hands = line.split(': ')
    defaults = {'red': 0, 'green': 0, 'blue': 0}
    for hand in hands.split('; '):
        for ball in hand.split(', '):
            count, color = ball.split(' ')
            if int(count) > defaults[color]:
                defaults[color] = int(count)

    secondamount += numpy.prod([*defaults.values()])

print(f'Second answer: {str(secondamount)}')