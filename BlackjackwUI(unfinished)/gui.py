import db,sys
from objects import Hand,Deck,Session
from datetime import datetime
import tkinter as tk
from tkinter import ttk


box = tk.Tk()
box.title("Blackjack")
box.geometry("500x500")

def player_win():
    winnings = bet
    new_balance = money.stopMoney + winnings
    results_text.set("You won")
    s.stopMoney = new_balance
    s.stopTime = datetime.now()
    db.add_session(s)
    db.close()
def player_loss():
    losing_balance = money.stopMoney - bet
    results_text.set("Sorry.You Lost")
    s.stopMoney = losing_balance
    s.stopTime = datetime.now()
    db.add_session(s)
    db.close()
def tie():
    results_text.set("Its a tie")
    s.stopMoney = money.stopMoney
    s.stopTime = datetime.now()
    db.add_session(s)
    db.close()
def player_blackjack():
    winnings = 1.5 * bet
    new_balance = money.stopMoney + winnings
    results_text.set("BLACKJACK")
    s.stopMoney = new_balance
    s.stopTime = datetime.now()
    db.add_session(s)
    db.close()

def stand():
    while dealer_hand.total() < 17:
        dealer_hand.add_card(deck.deal())
        dealer_hand.ace_adjust()
    if dealer_hand.total() > player_hand.total() and dealer_hand.total() < 22:
        player_loss()

    elif dealer_hand.total() > player_hand.total() and dealer_hand.total() > 21:
        player_win()

    elif player_hand.total() > dealer_hand.total():
        player_win()

    elif player_hand.total() == dealer_hand.total():
        tie()

def hit():
    player_hand.add_card(deck.deal())
    player_hand.ace_adjust()

    if dealer_hand.total() < 17:
        dealer_hand.add_card(deck.deal())
        dealer_hand.ace_adjust()
    show_hands()
    dealer_points_text.set(str(dealer_hand.total()))
    player_points_text.set(str(player_hand.total()))

    if player_hand.total() > dealer_hand.total() and player_hand.total() < 22:
        player_win()
    elif player_hand.total() > 21:
        player_loss()


def show_hands():
    dealer = ""
    player = ""

    for card in dealer_hand:
        dealer += str(card)

    dealer_cards_text.set(dealer)

    for card in player_hand:
        player += str(card)
    player_cards_text.set(player)

def exit():
    endTime = datetime.now()
    s.stopTime = endTime

    db.add_session(s)
    db.close()
    sys.exit()

def play():
    global s
    s = Session()
    startTime = datetime.now()
    s.startTime = startTime

    s.startMoney = float(moneytext.get())
    s.sessionID = 1 + money.sessionID

    global bet
    bet = betamount.get()
    if bet == "":
        results_text.set("Please Enter a Bet!")
    bet = float(bet)
    if bet  < 5:
        results_text.set("Minimum bet is $5,choose a new bet")
    elif bet > 1000 or bet > float(moneytext.get()):
        results_text.set("Bet cannot be larger than $1000 or current money balance, choose a new bet")



    deck.shuffle()
    dealer_hand.add_card(deck.deal())
    dealer_hand.ace_adjust()
    player_hand.add_card(deck.deal())
    player_hand.ace_adjust()
    player_hand.add_card(deck.deal())
    player_hand.ace_adjust()

    show_hands()
    dealer_points_text.set(str(dealer_hand.total()))
    player_points_text.set(str(player_hand.total()))

    if player_hand.total() == 21:
        player_blackjack()







global deck
deck = Deck()
global play_hand
player_hand = Hand()
global dealer_hand
dealer_hand = Hand()
#--------------------------Creates Money label and entry field
db.connect()
db.create_session()
global money
money = db.get_last_session()


moneytext = tk.StringVar()
moneylabel= ttk.Label(text="Money:").grid(column=0,row=0,padx=1,pady=5)
moneyentry= ttk.Entry(textvariable=moneytext,state="readonly",width=50).grid(column=1, row=0,columnspan=2)
moneytext.set(money.stopMoney)
#----------------------------------------------------------------
betlabel= ttk.Label(text="Bet:").grid(column=0,row=1,padx=1,pady=5)

betamount = tk.StringVar()
betentry= ttk.Entry(textvariable=betamount,width=50).grid(column=1, row=1,columnspan=2)

#-------------------------------------------------------------------------
dealerlabel= ttk.Label(text="DEALER").grid(column=0,row=2,padx=5,pady=5)

dealer_cards_text = tk.StringVar()
dealer_cards_label= ttk.Label(text="Cards:").grid(column=0,row=3,padx=5,pady=5)
dealer_cards_entry= ttk.Entry(textvariable=dealer_cards_text,state="readonly",width=50).grid(column=1, row=3, columnspan=2)

dealer_points_text = tk.StringVar()
dealer_points_label= ttk.Label(text="Points:").grid(column=0,row=4,padx=5,pady=5)
dealer_points_entry= ttk.Entry(textvariable=dealer_points_text,state="readonly",width=50).grid(column=1, row=4, columnspan=2)

#---------------------------------------------------
playerlabel= ttk.Label(text="PLAYER").grid(column=0,row=5,padx=5,pady=5)

player_cards_text = tk.StringVar()
player_cards_label= ttk.Label(text="Cards:").grid(column=0,row=6,padx=5,pady=5)
player_cards_entry= ttk.Entry(textvariable=player_cards_text,state="readonly",width=50).grid(column=1, row=6, columnspan=2)

player_points_text = tk.StringVar()
player_points_label= ttk.Label(text="Points:").grid(column=0,row=7,padx=5,pady=5)
player_points_entry= ttk.Entry(textvariable=player_points_text,state="readonly",width=50).grid(column=1, row=7, columnspan=2)

#---------------------------------------------------------
hit_button = ttk.Button(text="Hit", command=hit ).grid(column=0,row=8,columnspan=2,padx=5,pady=5)

stand_button = ttk.Button(text="Stand", command=stand ).grid(column=1,row=8,columnspan=2,padx=5,pady=5)
#----------------------------------------------------------

results_text = tk.StringVar()
results_label= ttk.Label(text="RESULT:").grid(column=0,row=9,padx=5,pady=5)
results_entry= ttk.Entry(textvariable=results_text,state="readonly",width=50).grid(column=1, row=9, columnspan=2)

#-----------------------------------------------------------
play_button = ttk.Button(text="Play", command=play).grid(column=0,row=10,columnspan=2,padx=1,pady=5)

Exit_button = ttk.Button(text="Exit", command= exit).grid(column=1,row=10,columnspan=2,padx=1,pady=5)



box.mainloop()