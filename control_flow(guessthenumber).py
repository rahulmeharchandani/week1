print("Welcome to the Number Guessing Game!")
print("I have selected a secret number between 1 and 100.")
num_to_guess=77
while True:
    guess=int(input("Please guess the number = "))
    if guess<num_to_guess:
        print("The guessed number is too low, please try again next time")
    elif guess>num_to_guess:
        print("The guessed number is too high, please try again next time")
    else:
        print("The guessed number is correct")
        print("you won  ")   
        break
    

    
