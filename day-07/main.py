lines = open("input.txt").readlines()

firstamount = 0
secondamount = 0

###

hands = []
for line in lines:
    hand, bid = line.split()
    
    occurences = [hand.count(card) for card in hand]

    score = 0
    if 5 in occurences:
        score = 6
    elif 4 in occurences:
        score = 5
    elif 3 in occurences:
        score = 3
        if 2 in occurences:
            score = 4
    elif occurences.count(2) == 4:
        score = 2
    elif 2 in occurences:
        score = 1

    hands.append((hand, int(bid), int(score)))


hands.sort(key=lambda hand: (hand[2],[x.replace("J","B").replace("Q","C").replace("K","D").replace("A","E").replace("T","A") for x in hand[0]]))

for index, (hand, bid, score) in enumerate(hands, 1):
    firstamount += index * bid

###
print(f'First answer: {str(firstamount)}')

###
# PART ONE WAS UGLY AS ***, And did not work for Part 2. I should really try functions more
letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}


def score(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def replacements(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in replacements(hand[1:])
    ]


def classify(hand):
    return max(map(score, replacements(hand)))


def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])


plays = []

for line in lines:
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key=lambda play: strength(play[0]))


for rank, (hand, bid) in enumerate(plays, 1):
    secondamount += rank * bid


###
print(f'Second answer: {str(secondamount)}')


