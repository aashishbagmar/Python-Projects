# import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False

def clear():  # Prints 50 blank lines
    print("\n" * 50)


def finding_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")

while not bidding_finished :
    name = input("What is your name?")
    price = int(input("What is your bid $"))
    bids[name] = price
    should_continue = input("Are there any bidder 'yes or 'no'.")
    if should_continue == "no":
        clear()
        bidding_finished = True
        finding_highest_bidder(bids)
    elif should_continue == "yes":
        clear() 











