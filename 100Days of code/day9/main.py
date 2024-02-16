#from replit import clear
from art import logo 
print(logo)


#HINT: You can call clear() to clear the output in the console.

bids = {}
def highest_bid(dict):
    current_max =0
    name = " "
    for key in dict:
        if  dict[key]>current_max:
            current_max= dict[key]
            name = key
    print(f"The winner is {name} with a bid of ${current_max}")

more_bids = True

while more_bids == True:
    name = input("What is your anme?: ")
    bid_amount =  round(float(input("What is your bid?: $")),2)
    bids[name]=bid_amount
    anyone_else = input("Are there anymore bidders? Type 'yes' or 'no'.").lower()
    if anyone_else == "no":
        highest_bid(bids)
        more_bids= False
        pr
       
