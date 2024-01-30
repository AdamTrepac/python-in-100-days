# blackjack game

from functools import total_ordering
import random
from tabnanny import check
from art import logo

############### Our Blackjack House Rules #####################

## DONE The deck is unlimited in size. 
## DONE There are no jokers. 
## DONE The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## DONE Use the following list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## DONE The cards in the list have equal probability of being drawn.
## DONE Cards are not removed from the deck as they are drawn.

# rules:
# 1. deal two cards to player and dealer
# 2. show dealers first card only
# 3. Ask user to hit
# 4. If they go over, end the game. Else
# 5. Ask if they want to hit again
# 6. Have dealer play until they have enough cards to beat the user, or break

# Assumptions:
# 1. Infinite deck - make choosing the cards easier, don't need to track random cards
# 2. Assume ace = 11 - can make this behavior more complicated later


def new_card(cards, amount):
    for _ in range(amount):
        cards += [random.randint(0, 12)] # 13 is the number of distinct cards in the deck
    return cards

# lost = check_loss(cards, card_dict) # temp spot for function to check if player won or lost    

# # function to return a true/false value if someone goes over, not implemented
# def card_overflow(cards, card_dict):
#     total_value = 0
#     for card in cards:
#         total_value += card_dict[card]
#     if total_value > 21:
#         return True
#     return False

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

def print_player_cards(cards):
    card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    print("Your cards:", end = " ")
    for index in cards:
        print(card_list[index], end = " ")
    print()

def print_dealer_cards(cards):
    card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    print("The dealer's cards:", end = " ")
    for index in cards:
        print(card_list[index], end = " ")
    print()

def player_turn(player_cards):
    another_card = input("Type y to get another card, type n to pass: ")
    while another_card == "y":
        player_cards = new_card(player_cards, 1)
        print_player_cards(player_cards)
        if check_value(player_cards) > 21:
            print("you went over, you lost")
            return []
        another_card = input("Type y to get another card, type n to pass: ")
    return player_cards

def dealer_turn(player_cards, dealer_cards):
    # 1. Show both cards
    # 2. If total is >= 17, stand and compare to user
    # 3. If total is < 17, take another card and re-compute

    print_dealer_cards(dealer_cards) # show both of dealers cards
    while (check_value(dealer_cards)) < 17:
        dealer_cards = new_card(dealer_cards, 1)
        print_dealer_cards(dealer_cards)
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
print_player_cards(player_cards)

dealer_cards = []
dealer_cards = new_card(dealer_cards, 2)
print_dealer_cards(dealer_cards[:1])

# # Ask user to hit
player_cards = player_turn(player_cards)

# Dealer actions:
if player_cards:
    dealer_turn(player_cards, dealer_cards)

print("Thanks for playing")
