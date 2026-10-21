import random
     
hidden_number = random.randint(1,100)
for I in range (10):
    guess = int(input ("Choose a number between 1-100. "))
    if guess == hidden_number:
        print ("You got it right, congratulations!")
    elif guess > hidden_number:
        print("Your number was too high.")
    elif hidden_number > guess:
        print("Your number was too low.")
else:
    print("You lost the game. You should try again!")