# blackjack game

from functools import total_ordering
import random
from subprocess import check_call
from tabnanny import check
from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

# rules:
# 1. deal two cards to player and dealer
# 2. show dealers first card only
# 3. Ask user to hit
# 4. If they go over, end the game. Else
# 5. Ask if they want to hit again
# 6. Have dealer play until they have enough cards to beat the user, or break

def new_card(cards, amount):
    for _ in range(amount):
        cards += [random.randint(0, 12)] # 13 is the number of distinct cards in the deck
    return cards  

def check_value(cards):
    card_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
    total_value = 0

    for card in cards:
        total_value += card_value[card]
    if total_value > 21:            # check for high aces to convert to low aces
        for i in range(len(cards)):
            if cards[i] == 0:
                cards[i] = 13
                total_value = check_value(cards)
                break
    return total_value

def check_blackjack(player_cards, dealer_cards):
    player_blackjack = False
    dealer_blackjack = False
    if check_value(player_cards) == 21:
        player_blackjack = True
    if check_value(dealer_cards) == 21:
        dealer_blackjack = True
    
    if not player_blackjack and not dealer_blackjack:
        return False
    elif player_blackjack and dealer_blackjack: 
        print("Both the dealer and player have a blackjack, the game ends in a draw")
    elif player_blackjack:
        print("The player wins with a blackjack!")
    else:
        print("The dealer has a blackjack, you lose")

    return True

def print_cards(cards, text):
    card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    print(text, end = " ")
    for index in cards:
        print(card_list[index], end = " ")
    print()

def player_turn(player_cards):
    another_card = input("Type y to get another card, type n to pass: ") # draw another card
    while another_card == "y":
        player_cards = new_card(player_cards, 1)
        print_cards(player_cards, "Your cards: ")
        if check_value(player_cards) > 21:
            print("you went over, you lost")
            return []
        another_card = input("Type y to get another card, type n to pass: ")
    return player_cards

def dealer_turn(player_cards, dealer_cards):
    # 1. Show both cards
    # 2. If total is >= 17, stand and compare to user
    # 3. If total is < 17, take another card and re-compute

    print_cards(dealer_cards, "The dealer's cards: ") # show both of dealers cards
    while (check_value(dealer_cards)) < 17:
        dealer_cards = new_card(dealer_cards, 1)
        print_cards(dealer_cards, "The dealer's cards: ")
        if check_value(dealer_cards) > 21:
            print("The dealer went over, you won!")
            return

    if check_value(dealer_cards) >= check_value(player_cards):
        print("Your card value does not surpass the dealer, you lose")
        return

    print("You surpassed the dealers hand, you won!")
    return
    
print(logo)

player_cards = []
player_cards = new_card(player_cards, 2)
print_cards(player_cards, "Your cards: ")

dealer_cards = []
dealer_cards = new_card(dealer_cards, 2)
print_cards(dealer_cards[:1], "The dealer's first card: ")

if not check_blackjack(player_cards, dealer_cards):
    # # Ask user to hit
    player_cards = player_turn(player_cards)

    # Dealer actions:
    if player_cards: # if the player cards are not empty, the game continues 
        dealer_turn(player_cards, dealer_cards)

print_cards(player_cards, "Your final cards: ")
print_cards(dealer_cards, "The dealer's final cards: ")
print("Thanks for playing")
