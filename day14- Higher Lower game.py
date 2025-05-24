import random
score = 0
#dict for having data
personalities = {
    "Cristiano Ronaldo" : {
        "Followers" : 652,
        "Country" : "Portugal",
        "Industry" : "Football(Soccer)"
    },
    "Lionel Messi" : {
        "Followers" : 505,
        "Country" : "Argentina",
        "Industry" : "Football(Soccer)"
    },
     "Selena Gomez" : {
        "Followers" : 421,
        "Country" : "USA",
        "Industry" : "Musician and Actress"
    },
    "Dwayne Johnson" : {
        "Followers" : 394,
        "Country" : "USA",
        "Industry" : "Actor & Former Wrestler"
    },
    "Kylie Jenner" : {
        "Followers" : 394,
        "Country" : "USA",
        "Industry" : "Media Personality & Entrepreneur"
    },
    "Ariana Grande" : {
        "Followers" : 376,
        "Country" : "USA",
        "Industry" : "Musician and Actress"
    },
    "Kim Kardashian" : {
        "Followers" : 357,
        "Country" : "USA",
        "Industry" : "Media Personality & Entrepreneur"
    },
    "Beyoncé" : {
        "Followers" : 312,
        "Country" : "USA",
        "Industry" : "Musician & Actress"
    },
    "Khloé Kardashian" : {
        "Followers" : 303,
        "Country" : "USA",
        "Industry" : "Media Personality"
    },
    "Nike" : {
        "Followers" : 301,
        "Country" : "USA",
        "Industry" : "Sportswear Brand"
    },

}
#function for extacting data of the person
names_person = list(personalities.keys())

def extract_data():
  global names_person
  if not names_person: # Check if the list is empty before choosing
      return None # Or handle the end of the game here
  x = random.choice(names_person)
  x_score = personalities[x]["Followers"]
  x_industry = personalities[x]["Industry"]
  details = [x,x_score,x_industry]
  names_person.remove(x)
  return details

#fuction for asking users choice

def ask_user(person1_data): # Accept person1 data as an argument
  global score
  
  person2_data = extract_data() # Extract data for the second person

  # Handle the case where extract_data returns None (no more personalities)
  if person2_data is None:
      print(f"Your highest score is : {score}")
      return False # Indicate game over

  print(f" It's {person1_data[0]} VS {person2_data[0]}")
  user_opinion = input(f"Does {person2_data[0]} have more followers? Type 'H' for higer and 'L' for otherwise.").upper()
  user_num = 0
  if user_opinion == 'H':
    user_num = 1
  else: 
    user_num = -1
        
  #function to evaluate the choice and update score
  if (person1_data[1] < person2_data[1] and user_num == 1) or (person1_data[1] > person2_data[1] and user_num == -1):
    score += 1
    print("Correct!")
    return person2_data # Return the data of the second person for the next round
  else: 
    score = 0
    print("You got it wrong!!\n Game Over.")
    return False # Indicate game over

# If user succeds, continue the loop
def play_game():
  global score, names_person
  
  # Start with the first person
  current_person = extract_data()
  if current_person is None:
      print("Not enough personalities to play.")
      return

  # Loop until the user gets it wrong or runs out of personalities
  while True:
      result = ask_user(current_person)
      if result is False: # Game is over
          break
      else: # User was correct, continue with the second person as the new first person
          current_person = result
          print(f"Current score: {score}")
      
      # Check if we've used all personalities
      if not names_person:
          print(f"You've compared everyone! Your final score is: {score}")
          break

play_game()
