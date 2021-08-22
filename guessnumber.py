import random
print("Lets play guess the number game \n")

difficulty_level= input("Choose your Difficulty Level easy , hard? ").lower()
print("Choose number between 1 - 100 \n")

difficulty_attempts = {"hard":5, "easy":10}

hidden_number = random.randint(0,100)
print(hidden_number)
end_game = False
def play():
    guessed_number = int(input("Guess a number"))
    if guessed_number==hidden_number:
      end_game=True
      return end_game
    else:
      play()
for _ in range(0,difficulty_attempts[difficulty_level]):
  if(play()):
    print( "You won")

  

