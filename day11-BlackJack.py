import random
import os
from time import sleep
l = [2,3,4,5,6,7,8,9,{'A': 11},{'K': 10},{'Q':10},{'J':10},]
m = [2,3,4,5,6,7,8,9,{'A': 11},{'K': 10},{'Q':10},{'J':10},]

#pop out the card#
#work on ace card#
#test the while loop#

player_cards = []
dealer_cards = []

game_over:bool = False

def user_score(user_list):
    score = sum(user_list)
    if score > 21:
        for card in user_list:
            if card == 11:
                score -= 10
    return score

player_score = user_score(player_cards)
dealer_score = user_score(dealer_cards)


def draw_cards(user_cards,l):
    card = random.choice(l)
    x = isinstance(card,dict)
    if x:
          user_cards.append(list(card.values())[0])
    else:
          user_cards.append(card)
    l.remove(card)
        
    return user_cards

def check_score(player_score,dealer_score):
    # global player_score,dealer_score
    player_score = user_score(player_cards)
    dealer_score = user_score(dealer_cards)
    if player_score == dealer_score:
        print("Its a Draw")
    if player_score > 21:
        if dealer_score > 21:
            print("Draw")
        else :
            print("Dealer Wins ")
    else:
        if dealer_score > 21:
            print("You Win, Horray!!")
        else :
            if player_score > dealer_score:
                print("You Win, Horray!!")
            else:
                print("Dealer Wins ")

    print(f"Players Cards were: {player_cards}, Total points = {player_score}")
    print(f"Dealers Cards were: {dealer_cards}, Total points = {dealer_score}")
    game_over = True
#    return -1

def clr():
    sleep(5)
    os.system('clear')

def output_scores(player_score,dealer_score):
    # global player_score,dealer_score
    player_score = user_score(player_cards)
    dealer_score = user_score(dealer_cards)
    print(f"\nPlayer has the cards: {player_cards}. Total score = {player_score} \n")

    print(f"Dealer has the card: {dealer_cards[0]}.\n")
    clr()
    if player_score >= 21:
        check_score(player_score,dealer_score)
def dealers_play(dealer_score,dealer_cards):
    # global dealer_score,dealer_cards
    dealer_score = user_score(dealer_cards)
    if dealer_score < 17:
        dealer_cards = draw_cards(dealer_cards,l)
    else:
        return



print("Welcome to the ...BlackJack... Game!")
for i in range(0,2):
    player_cards = draw_cards(player_cards,l)
    dealer_cards = draw_cards(dealer_cards,l)



while 1:
  if game_over == True:
      break
  else:
      output_scores(player_score,dealer_score)
      if game_over == True:
            break
      want_card = input("Type 'y' to get a card or 'n' to pass")
      if want_card == 'y':
          player_cards = draw_cards(player_cards,l)
      else:
          dealers_play(dealer_score,dealer_cards)
          check_score(player_score,dealer_score)
          break
        

print("See you in the next game!")




