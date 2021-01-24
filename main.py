from replit import clear
import art
print(art.logo)

print("Welcome to secret auction program.")

bid={}
bidding_finished=False

def checkhighest(biddingrecord):
    highest_bid=0
    winner=""
    for bidder in biddingrecord:
      bid_amount=biddingrecord[bidder]
      if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  bidder1 = input("what is your name?: ")
  bid1= int(input("what's is your bid?: $"))
  bid[bidder1]=bid1
  bid_to_continue=input("Are there any other bidders? yes or no")
  if bid_to_continue=="yes":
    clear()
  else:
      bidding_finished=True
      checkhighest(bid)
  

  
















#HINT: You can call clear() to clear the output in the console.