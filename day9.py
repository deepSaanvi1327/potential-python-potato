''' cd work/git_demo/potential-python-potato '''
import os
from time import sleep

bidders = {}
any_bidders = 'True'
while (any_bidders == 'True'):
    name = input("Honoured Bidder, may I ask your name? : ")
    bid = int(input("How much are you willing to bid? :"))
    bidders[name] = bid
    left = input("Do you find any other bidders? [Yes -> True/No -> False] : ")
    print(left)
    any_bidder = left
    if any_bidder == 'False':
        break
        

    sleep(1)
    os.system('clear')
os.system('clear')

max_bid = 0
awardee = ""
for ppl in bidders:
    if bidders[ppl] > max_bid:
        max_bid = bidders[ppl]
        awardee = ppl

print(f"This bid is won by {awardee} with a heafty bid of {max_bid}\n")


        


