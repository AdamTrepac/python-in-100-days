# Write a program that collects the names and bids of different people. Use a dictionary to store the names

from silent_art import logo
import os

def bid_collection():
    while True:
        # Ask the user for their name and bid
        name = input("Please enter your name: ")
        bid = int(input("Please enter your bid: "))
        auction_dict[name] = bid

        # Ask if there are any more users - if yes then loop + clear the screen
        end_check = input("Are there any more bidders? (yes or no) ").lower()
        os.system('cls') # clear the screen
        if end_check == ("no"):
            break

def compute_winner():
    highest_bid = "temp_name"
    for name in auction_dict:
        if auction_dict[name] > auction_dict[highest_bid]:
            highest_bid = name
    
    return highest_bid

# Print the logo, welcome to the auction
print(logo)
print("Welcome to the silent auction")

auction_dict = {"temp_name": 0}
bid_collection()
# print(auction_dict) # debug to show all inputs

# If there are no more bidders, compute the winner
winner = compute_winner()
print(winner, "won the auction with the highest bid of:", auction_dict[winner])