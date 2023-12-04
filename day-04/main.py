lines = open("input.txt").readlines()

firstamount = 0
for line in lines:
    card, cardnumbers = line.split(':')
    winnumbers,setnumbers = cardnumbers.split('|')
    winnumbers,setnumbers = winnumbers.split(), setnumbers.split()
    
    wins = set(winnumbers) & set(setnumbers)
    if len(wins) > 0:
        firstamount += 2 ** (len(wins) - 1)

print(f'First answer: {str(firstamount)}')

secondamount = 0
cardcount = []
for x in lines:
    cardcount.append(1)

for cardnr,line in enumerate(lines):
    card, cardnumbers = line.split(':')
    winnumbers,setnumbers = cardnumbers.split('|')
    winnumbers,setnumbers = winnumbers.split(), setnumbers.split()
    
    wins = set(winnumbers) & set(setnumbers)
    for win in range(len(wins)):
        cardcount[cardnr + win + 1] += cardcount[cardnr] 
    secondamount = sum(cardcount)

print(f'Second answer: {str(secondamount)}')