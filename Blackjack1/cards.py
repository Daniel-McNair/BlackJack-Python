import random
def make_deck():
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = []
    for s in suit:
        for r in rank:
            deck.append(r + ' of ' + s)
    random.shuffle(deck)
    return deck

def deal(hand,deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)



def return_total(hand, total):

    for i in range(len(hand)):
        if hand[i][0] == "A":
            total += 11
        elif hand[i][0] == "2":
            total +=2
        elif hand[i][0] == "3":
            total +=3
        elif hand[i][0] == "4":
            total +=4
        elif hand[i][0] == "5":
            total +=5
        elif hand[i][0] == "6":
            total +=6
        elif hand[i][0] == "7":
            total +=7
        elif hand[i][0] == "8":
            total +=8
        elif hand[i][0] == "9":
            total +=9
        elif hand[i][0] == "1":
            total +=10
        elif hand[i][0] == "J":
            total +=10
        elif hand[i][0] == "Q":
            total +=10
        elif hand[i][0] == "K":
            total +=10
    return total





