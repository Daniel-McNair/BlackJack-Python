import db,cards,sys
print("BLACKJACK!")
print("Blackjack payout is 3:2 \n")

# reads money value from file
try:
    money = db.reading_money()
    print('Money:', money)
except:
    print(sys.exc_info()[0], 'Occurred')
    sys.exit()

def blackjack():
    # places bet with input validation
    while True:
        try:
            bet = float(input("Bet amount:"))

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
    print("DEALER\'S SHOW CARD: \n",dealer_hand)
    cards.deal(player_hand, deck)
    cards.deal(player_hand, deck)
    print("YOUR CARDS: \n",player_hand)
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

    winnings = round(1.5 * bet,2)
    new_balance = str(money + winnings)
    losing_balance = str(money - bet)
    if cards.return_total(player_hand, player_total) > cards.return_total(dealer_hand, dealer_total) and cards.return_total(player_hand, player_total) <= 21  or cards.return_total(dealer_hand, dealer_total) > 21 :
        print("You won $",bet)
        db.writing_money(new_balance)
    elif cards.return_total(player_hand, player_total) < cards.return_total(dealer_hand, dealer_total) and cards.return_total(dealer_hand, dealer_total) <= 21 or cards.return_total(player_hand, player_total) > 21 :
        print("You lost $", bet)
        db.writing_money(losing_balance)
    else:
        print("Its a tie")

    if db.reading_money() < 5:
        print("You are below the minimum balance")
        new_chips = float(input("How many chips would you like to purchase?"))
        chip_purchase = str(new_chips)
        db.writing_money(chip_purchase)



blackjack()
restart = input("Play Again? (y/n)").lower()
if restart == "y":
    blackjack()
else:
    print("Come back soon! \n Bye!")
    sys.exit()






