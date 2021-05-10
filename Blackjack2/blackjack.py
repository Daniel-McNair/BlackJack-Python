import db,cards,sys,locale
from datetime import datetime, timedelta
from decimal import Decimal
locale = locale.setlocale(locale.LC_ALL, "")
if locale == "C":
    locale.setlocale(locale.LC_ALL, "en_US")
print("BLACKJACK!")
print("Blackjack payout is 3:2")
startTime = datetime.now()
print("Start Time:", startTime.strftime("%X"),"\n")
# reads money value from file
try:
    money = Decimal(db.reading_money())
    print('Money:', locale.currency(money, grouping=True))
except:
    print(sys.exc_info()[0], 'Occurred')
    sys.exit()

def blackjack():
    # places bet with input validation
    while True:
        try:
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
    deck = cards.make_deck()
    dealer_hand = []
    player_hand = []
    player_total = 0
    dealer_total = 0
    cards.deal(dealer_hand, deck)
    print("\nDEALER\'S SHOW CARD: \n",dealer_hand)
    cards.deal(player_hand, deck)
    cards.deal(player_hand, deck)
    print("\nYOUR CARDS: \n",player_hand)
    print("\nDealer Score:", cards.return_total(dealer_hand,dealer_total))
    print("Your Score:", cards.return_total(player_hand, player_total))

    while cards.return_total(dealer_hand, dealer_total) < 21 or cards.return_total(player_hand, player_total) < 21:
        response = str(input("Hit or stand? (hit/stand): "))
        if response == "hit":
            cards.deal(player_hand, deck)
            print("DEALER\'S SHOW CARD: \n", dealer_hand)
            print("YOUR CARDS: \n", player_hand)
            print("Dealer Score:", cards.return_total(dealer_hand, dealer_total))
            print("Your Score:", cards.return_total(player_hand, player_total))
            if cards.return_total(player_hand, player_total) > 20:
                break
        elif cards.return_total(dealer_hand, dealer_total) < 17:
            cards.deal(dealer_hand, deck)
            print("DEALER\'S SHOW CARD: \n", dealer_hand)
            print("YOUR CARDS: \n", player_hand)
            print("Dealer Score:", cards.return_total(dealer_hand, dealer_total))
            print("Your Score:", cards.return_total(player_hand, player_total))
            if cards.return_total(dealer_hand, dealer_total) > 20:
                break

        else:
            break

    winnings = round(Decimal(1.5) * bet,2)
    new_balance = str(money + winnings)
    losing_balance = str(money - bet)
    if cards.return_total(player_hand, player_total) > cards.return_total(dealer_hand, dealer_total) and cards.return_total(player_hand, player_total) <= 21  or cards.return_total(dealer_hand, dealer_total) > 21 :
        print("\nYou won $",bet)
        db.writing_money(new_balance)
        print("Money:",locale.currency(Decimal(new_balance), grouping=True))
    elif cards.return_total(player_hand, player_total) < cards.return_total(dealer_hand, dealer_total) and cards.return_total(dealer_hand, dealer_total) <= 21 or cards.return_total(player_hand, player_total) > 21 :
        print("\nYou lost $", bet)
        db.writing_money(losing_balance)
        print("Money:", locale.currency(Decimal(losing_balance), grouping=True))
    else:
        print("Its a tie")

    if db.reading_money() < 5:
        print("You are below the minimum balance")
        new_chips = Decimal(input("How many chips would you like to purchase?"))
        chip_purchase = str(new_chips)
        db.writing_money(chip_purchase)



blackjack()
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






