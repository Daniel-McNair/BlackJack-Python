import random
suits = ["Spades","Hearts","Clubs","Diamonds"]
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
rank_points = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, rank, suit, points):
        self.rank = rank
        self.suit = suit
        self.points = points

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit, rank_points[rank]))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck.pop()
        return card
    def count(self):
        return len(self.deck)

class Hand:
    def __init__(self):
        self.cards = []
        self.points = 0
        self.aces = 0

    def __iter__(self):
        self.iterate = -1
        return self
    def __next__(self):
        if self.iterate >= len(self.cards)-1:
            raise StopIteration()
        self.iterate += 1
        return self.cards[self.iterate]


    def add_card(self,card):
        self.cards.append(card)
        self.points += card.points
        if card.rank == 'Ace':
            self.aces += 1

    def ace_adjust(self):
        while self.points > 21 and self.aces >= 1:
            self.points -= 10
            self.aces -= 1

    def get_card(self,index):
        return self.cards[index]

    def count(self):
        return len(self.cards)

    def total(self):
        return self.points


class Session:
    def __init__(self, sessionID =0, startTime=None, startMoney=0, stopTime=None, stopMoney=0):
        self.sessionID = sessionID
        self.startTime = startTime
        self.startMoney = startMoney
        self.stopTime = stopTime
        self.stopMoney = stopMoney

