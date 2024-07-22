from art import logo
from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the blind auction")

users_dict = {}

def adding_new_bidder(users_dict, name, bid):
  users_dict[name] = bid

def bidding_game(users_dict):
  highest_score = 0
  for key in users_dict:
    if users_dict[key] > highest_score:
      highest_score = users_dict[key]
  for key in users_dict:
    if users_dict[key] == highest_score:
      print(f"The Winner is {key} with a bid of ${users_dict[key]}") 
      
def Game():
  bidding_finished = False
  while not bidding_finished:
    name_input = input("What is your name? ")
    bid_input = int(input("What is your bid? "))
    adding_new_bidder(users_dict, name_input, bid_input)
    bidding_choice = input("Are there any other bidders? Type yes or no ")
    if bidding_choice == "no":
      bidding_finished = True
      bidding_game(users_dict)
    elif bidding_choice == "yes":
      clear()

Game()
# for key in users_dict:
#   if(users_dict[key] == bidding_price):
#     print(f"The Winner is {key} with a bid of ${users_dict[key]}")
