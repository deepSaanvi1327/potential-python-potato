import random
#import os
#from time import sleep

is_game_over = False

def pick_a_number():
    x = random.randint(1,101)
    return x

def check_guess(protagonist_number,guess_number):
    global is_game_over
    difference = protagonist_number - guess_number

    if difference > 0:
        print("Too Low")
    elif difference < 0:
        print("Too High")
    else:
        print(f"You got it right! The number indeed was {protagonist_number}")
        is_game_over = True

def difficulty_level(chance,protagonist_number):
    for i in range(1,chance):
        if is_game_over == False:
            attempts = chance - i
            print(f"\nYou have {attempts} attempts left.")
            guess_num = int(input("Make a guess : "))
            check_guess(protagonist_number,guess_num)
        else:
            print("GAME OVER")
            break
    return





logo = """



▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖       ▗▖  ▗▖▗▖ ▗▖▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖      ▗▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖ ▗▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖     ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖
  █  ▐▌ ▐▌▐▌          ▐▛▚▖▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌     █  ▐▛▚▖▐▌▐▌       ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌   
  █  ▐▛▀▜▌▐▛▀▀▘       ▐▌ ▝▜▌▐▌ ▐▌▐▌  ▐▌▐▛▀▚▖▐▛▀▀▘▐▛▀▚▖    ▐▌▝▜▌▐▌ ▐▌▐▛▀▀▘ ▝▀▚▖ ▝▀▚▖  █  ▐▌ ▝▜▌▐▌▝▜▌    ▐▌▝▜▌▐▛▀▜▌▐▌  ▐▌▐▛▀▀▘
  █  ▐▌ ▐▌▐▙▄▄▖       ▐▌  ▐▌▝▚▄▞▘▐▌  ▐▌▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌    ▝▚▄▞▘▝▚▄▞▘▐▙▄▄▖▗▄▄▞▘▗▄▄▞▘▗▄█▄▖▐▌  ▐▌▝▚▄▞▘    ▝▚▄▞▘▐▌ ▐▌▐▌  ▐▌▐▙▄▄▖
                                                                                                                            
                                                                                                                            
                                                                  


"""
print(logo)

main_number = pick_a_number()

want_hard = input("Choose your difficulty- Easy or Hard ::  ").lower()

if want_hard == "hard":
    chances = 6
    difficulty_level(chances,main_number)
else:
    chances = 11
    difficulty_level(chances,main_number)

print(f"The number was {main_number}.")
    




















