import db,sys,locale
from objects import Hand,Deck
from datetime import datetime, timedelta
from decimal import Decimal
def show_time():
    local = locale.setlocale(locale.LC_ALL, "")
    if local == "C":
        local.setlocale(locale.LC_ALL, "en_US")
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    global startTime
    startTime = datetime.now()
    print("Start Time:", startTime.strftime("%X"),"\n")

def read_money():
    # reads money value from file
    try:
        global money
        money = Decimal(db.reading_money())
        print('Money:', locale.currency(money, grouping=True))
    except:
        print(sys.exc_info()[0], 'Occurred')
        sys.exit()

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.ace_adjust()
def place_bet():
    # places bet with input validation
    while True:
        try:
            global bet
            bet = Decimal(input("Bet amount:"))

        except ValueError:
            print(sys.exc_info()[0], 'Occurred, enter new bet')
            continue

        if bet < 5:
            print("Minimum bet is $5,choose a new bet")
        elif bet > 1000 or bet > money:
            print("Bet cannot be larger than $1000 or current money balance, choose a new bet")
        else:
            break

def show_hands(dealer_hand,player_hand):
    print("\nDEALER\'S SHOW CARD: ")
    for card in dealer_hand:
        print(card)

    print("\nYOUR CARDS: ")
    for card in player_hand:
        print(card)

def player_win():
    winnings = bet
    new_balance = str(money + winnings)
    print("\nYou won $", bet)
    db.writing_money(new_balance)
    print("Money:", locale.currency(Decimal(new_balance), grouping=True))

def player_loss():
    losing_balance = str(money - bet)
    print("\nYou lost $", bet)
    db.writing_money(losing_balance)
    print("Money:", locale.currency(Decimal(losing_balance), grouping=True))

def tie():
    print("Its a tie")

def player_blackjack():
    winnings = round(Decimal(1.5) * bet, 2)
    new_balance = str(money + winnings)
    print("\nBLACKJACK!!! \nYou won $", winnings)
    db.writing_money(new_balance)
    print("Money:", locale.currency(Decimal(new_balance), grouping=True))
def blackjack():
    show_time()
    read_money()
    place_bet()
    deck = Deck()
    deck.shuffle()
    dealer_hand = Hand()
    hit(deck, dealer_hand)
    player_hand = Hand()
    hit(deck, player_hand)
    hit(deck, player_hand)
    show_hands(dealer_hand, player_hand)
    print("\nDealer Score:", dealer_hand.total())
    print("Your Score:", player_hand.total())
    if player_hand.total() == 21:
        player_blackjack()
        restart()
    while dealer_hand.total() < 17:
        hit(deck, dealer_hand)

    while player_hand.total() <= 21:
        response = str(input("Hit or stand? (hit/stand): "))
        if response == "hit":
            hit(deck, player_hand)
            show_hands(dealer_hand, player_hand)
            print("\nDealer Score:", dealer_hand.total())
            print("Your Score:", player_hand.total())
            if player_hand.total() > dealer_hand.total() and player_hand.total() < 22:
                player_win()
                restart()
            elif player_hand.total() > 21:
                player_loss()
                restart()
        elif response == "stand":
            show_hands(dealer_hand, player_hand)
            print("Dealer Score:", dealer_hand.total())
            print("Your Score:", player_hand.total())
            if dealer_hand.total() > player_hand.total() and dealer_hand.total() < 22:
                player_loss()
                restart()
            elif dealer_hand.total() > player_hand.total() and dealer_hand.total() > 21:
                player_win()
                restart()
            elif player_hand.total() > dealer_hand.total():
                player_win()
                restart()
            elif player_hand.total() == dealer_hand.total():
                tie()
                restart()

    # if after a hit the player is less than dealer, player can hit or stand again
        if player_hand.total() < dealer_hand.total():
            response = str(input("Hit or stand? (hit/stand): "))
            if response == "hit":
                hit(deck, player_hand)
                show_hands(dealer_hand, player_hand)
                print("\nDealer Score:", dealer_hand.total())
                print("Your Score:", player_hand.total())
                if player_hand.total() > dealer_hand.total() and player_hand.total() < 22:
                    player_win()
                    restart()
                elif player_hand.total() > 21:
                    player_loss()
                    restart()
            elif response == "stand":
                show_hands(dealer_hand, player_hand)
                print("Dealer Score:", dealer_hand.total())
                print("Your Score:", player_hand.total())
                if dealer_hand.total() > player_hand.total() and dealer_hand.total() < 22:
                    player_loss()
                    restart()
                elif dealer_hand.total() > player_hand.total() and dealer_hand.total() > 21:
                    player_win()
                    restart()
                elif player_hand.total() > dealer_hand.total():
                    player_win()
                    restart()
                elif player_hand.total() == dealer_hand.total():
                    tie()
                    restart()




def restart():
    if db.reading_money() < 5:
        print("You are below the minimum balance")
        new_chips = Decimal(input("How many chips would you like to purchase?"))
        chip_purchase = str(new_chips)
        db.writing_money(chip_purchase)
    restart = input("\nPlay Again? (y/n)").lower()
    if restart == "y":
        blackjack()
    else:
        endTime = datetime.now()
        print("\nStop Time:", endTime.strftime("%X"))
        timeElapsed = endTime - startTime
        print("Elapsed Time:", str(timedelta(seconds=timeElapsed.seconds)))
        print("\nCome back soon! \nBye!")
        sys.exit()

def main():
    blackjack()

if __name__ == "__main__":
    main()