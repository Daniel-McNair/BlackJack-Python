import random
cards = {'Hearts':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11},
         'Diamonds':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11},
         'Spades':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11},
         'Clubs':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}}

def make_deck():
    deck = []
    for outer_key in cards:
        for inner_key in cards[outer_key]:
            deck.append(('{} of {}'.format(inner_key,outer_key)))
    random.shuffle(deck)
    return deck

def deal(hand,deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)



def return_total(hand, total):

    for i in range(len(hand)):
        if "Ace" in hand[i]:
            total += 11
        elif "Two" in hand[i]:
            total +=2
        elif "Three" in hand[i]:
            total +=3
        elif "Four" in hand[i]:
            total +=4
        elif "Five" in hand[i]:
            total +=5
        elif "Six" in hand[i]:
            total +=6
        elif "Seven" in hand[i]:
            total +=7
        elif "Eight" in hand[i]:
            total +=8
        elif "Nine" in hand[i]:
            total +=9
        elif "Ten" in hand[i]:
            total +=10
        elif "Jack" in hand[i]:
            total +=10
        elif "Queen" in hand[i]:
            total +=10
        elif "King" in hand[i]:
            total +=10
    return total





