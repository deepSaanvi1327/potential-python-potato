import random
stage = [
'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
_____|___''' ,
'''
    
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
_____|___''' ,
'''
    
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
_____|___''',
'''
    
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |       
     |
_____|___''',
'''
    
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |       
     |
_____|___''',
'''
    
      _______
     |/      |
     |      (_)
     |       |
     |       
     |       
     |
_____|___''',]

word = ["abbreviate","serendipity","affluently","bafflement" ] #,"carpooling"

chosen_word = random.choice(word)

#print(chosen_word)

length = len(chosen_word)
l_cpy = length
place_holder = ["_ "] * length 
                                         #Generating a place holder (measurements)
unique_letters = list(chosen_word)

print(f"[[{' '.join(place_holder)}]]")

life  = 0



for i in range(0,length):
    #j = i+1
    for j in range(i+1,l_cpy):
        if unique_letters[i] == unique_letters[j]:      #Check for number of times the loop has to be iterated
            unique_letters.pop(j)
            l_cpy -= 1
            break
            

#print(unique_letters)

unique_count = len(unique_letters)  

for i in range(0, unique_count):
    print(f"You have {6-life} lifes left. And {unique_count-i} chances to guess!")
    if life == 5:
       print(" you loose!!")
       print(f"Word was {chosen_word}")
       quit()

    else:
        guess = input("Make a guess letter: ").lower()

        if guess in chosen_word:
            for j in range(0,length):
                if j!= length:
                    if guess == chosen_word[j]:
                        place_holder[j] = guess
                        

        else:
           life += 1
           
           #break 
    print(f"[[{' '.join(place_holder)}]]") #print(' '.join(a))
    print(stage[life])
    print("-------------------------")
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

if life <= 5 and "_ " not in place_holder:
    print("You are still alive!!")
else:
    print("You loose!!")
    print(f"Word was {chosen_word}")

