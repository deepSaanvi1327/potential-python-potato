import random
import os
from time import sleep



def deal_card():
    """Pick out random cards """
    l = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(l)
    return card


def calculate_scores(deck_of_cards):
    """Takes in a list of cards """
    score = sum(deck_of_cards)
    if score == 21 and len(deck_of_cards) == 2:
        return 0
    if score > 21 and 11 in deck_of_cards:
        score -= 10
    return score

def is_player_winner(score1, score2):
    """Takes 2 integer values, checks if the player(score1) won"""
    if score1 < 21:
        if score1 == 0:
            print("You Won , its a Black Jack🥳")
#            return 1
        elif score1 == score2:
            print("Its a Draw.🤡")
#            return -1
        elif score1 < score2:
             
                print("You Loose😭 , your opponent outpassed you")
        else:
            if score1 > score2 :
                print("You Won , you outpassed your opponent🥳")
#                return 1
    elif score1 == 21:
        print("You Won , its a full score🥳")
#        return 1
    else:
        if score2 <= 21:
            print("You Loose!😭 You have outpassed the limit")
#            return 0
        else:
            print("Its a Draw,🤡 both of you have exceeded the limit")
#            return -1
            


user_card = []
computer_card = []
user_score = -1
computer_score = -1
is_game_over = False

for i in range(0,2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

while not is_game_over:

    user_score = calculate_scores(user_card)
    computer_score = calculate_scores(computer_card)
    print(f"\n\nYour cards : {user_card}, current score = {user_score}")
    print(f"Dealers first card : {computer_card[0]}.")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to draw another card 'n' to pass  :: ")
        if user_should_deal == "y":
            user_card.append(deal_card())
        else: 
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_scores(computer_card)

user_score = calculate_scores(user_card)
computer_score = calculate_scores(computer_card)

is_player_winner(user_score, computer_score)


print("\n GAME OVER")
print(f"Dealers cards were {computer_card}, Total score = {calculate_scores(computer_card)}")




















