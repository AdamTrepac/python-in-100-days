# blackjack game

from functools import total_ordering
import random
from tabnanny import check
from art import logo

# rules:
# 1. deal two cards to player and dealer
# 2. show dealers first card only
# 3. Ask user to hit
# 4. If they go over, end the game. Else
# 5. Ask if they want to hit again
# 6. Have dealer play until they have enough cards to beat the user, or break

# Assumptions:
# 1. Infinite deck - make choosing the cards easier, don't need to track random cards
# 2. Assume ace = 10 - can make this behavior more complicated later



def another_one(cards, card_dict, card_list):
    cards += random.choices(card_list)
    lost = check_loss(cards, card_dict)
    return lost, cards
    
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
    return total_value

card_dict = {"A": 1, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3":3, "2":2}
card_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

player_cards = random.choices(card_list, k=2)
print(player_cards)

dealer_cards = random.choices(card_list, k=2)
print(dealer_cards[0])

# Ask user to hit
another_card = input("Type y to get another card, type n to pass: ")
while another_card == "y":
    game_over, player_cards = another_one(player_cards, card_dict, card_list)
    if game_over == True:
        print("game_over", player_cards)
        break
    else:
        print(player_cards)
    another_card = input("Type y to get another card, type n to pass: ")

# Dealer actions:
# 1. Show both cards
# 2. If total is >= 17, stand and compare to user
# 3. If total is < 17, take another card and re-compute
print(dealer_cards) # show both of dealers cards
while (check_value(dealer_cards,card_dict)) < 17:
    game_over, dealer_cards = another_one(dealer_cards, card_dict, card_list)
    print(dealer_cards)
    if game_over == True:
        print("The dealer went over, you won!")
        break
    elif check_value(dealer_cards, card_dict) >= check_value(player_cards, card_dict):
        print("Your card value does not pass the dealer, you lose")

print("Thanks for playing")

