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
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
    weights =   [1 , 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1 , 1 , 1 , 0]

    cards += random.choices(card_list, k = amount, weights = weights)
    return cards

# lost = check_loss(cards, card_dict) # temp spot for function to check if player won or lost    

def check_loss(cards, card_dict):
    total_value = 0
    for card in cards:
        total_value += card_dict[card]
    if total_value > 21:
        return True
    return False

def check_value(cards, card_dict):
    total_value = 0
    for card in cards:
        total_value += card_dict[card]
    # if total_value > 
    return total_value

def print_player_cards(cards):
    card_dict = {11: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 10: , 10, 10, 1}
    print("Your cards:", end = " ")
    for card in cards:
        print(card, end = " ")
    print()

def print_dealer_cards(cards):
    print("The dealer's cards:", end = " ")
    for card in cards:
        print(card, end = " ")
    print()

def player_turn(player_cards, card_dict, card_list):
    game_over = False
    
    another_card = input("Type y to get another card, type n to pass: ")
    while another_card == "y":
        game_over, player_cards = new_card(player_cards, card_dict, card_list)
        print_player_cards(player_cards)
        if game_over == True:
            print("you went over, you lost")
            return game_over, player_cards
        another_card = input("Type y to get another card, type n to pass: ")
    return game_over, player_cards

def dealer_turn(player_cards, dealer_cards, card_dict, card_list):
    # 1. Show both cards
    # 2. If total is >= 17, stand and compare to user
    # 3. If total is < 17, take another card and re-compute
    game_over = False

    print_dealer_cards(dealer_cards) # show both of dealers cards
    while (check_value(dealer_cards,card_dict)) < 17:
        game_over, dealer_cards = new_card(dealer_cards, card_dict, card_list)
        print_dealer_cards(dealer_cards)
        if game_over == True:
            print("The dealer went over, you won!")
            return game_over, dealer_cards

    if check_value(dealer_cards, card_dict) >= check_value(player_cards, card_dict):
        print("Your card value does not surpass the dealer, you lose")
        game_over = True
        return game_over, dealer_cards

    print("You surpassed the dealers hand, you won!")
    return game_over, dealer_cards
    

# card_dict = {"A": 11, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3":3, "2":2}
# card_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]


print(logo)

player_cards = []
player_cards = new_card(player_cards, 2)
print_player_cards(player_cards)

dealer_cards = []
dealer_cards = new_card(dealer_cards, 2)
print("The first dealer's card: ",dealer_cards[0])

# # Ask user to hit
game_over, player_cards = player_turn(player_cards, card_dict, card_list)

# # Dealer actions:
# if game_over == False:
#     dealer_turn(player_cards, dealer_cards, card_dict, card_list)

# print("Thanks for playing")

