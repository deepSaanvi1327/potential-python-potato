import random
scissors = '''
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === | '''
rock = '''
    _______
---'   ____)
      (|____)
      (|____)
      (|___)
---.__(|__)
'''
paper = '''
   _________
---'   _____)_____
          ________)
          _________)
         _________)
---.____________)

'''
comp_input = random.randint(1,3)    # integer

game = [rock, paper , scissors]

print("ROCK PAPER SCISSORS !!! The Game starts\n 1 -> Rock\n 2 -> Paper\n 3 -> Scissors")
player_input = int(input("What do you choose?   "))    #integer

if player_input > 3:
    print("Type 1,2,3 only")
    exit()


else:
    print(f"Your move {game[player_input - 1]}")
    print(f"Computers move {game[comp_input - 1]}")
    print("\n")

    if player_input == 1 and comp_input == 3:
        print("         You Win")
    elif player_input == 3 and comp_input == 1:
        print("         You loose!!!")
    elif player_input > comp_input :
        print("         You Win")

    elif player_input == comp_input :
        print("         Its a Draw!!")
    else:
        print("         You loose!!!")
