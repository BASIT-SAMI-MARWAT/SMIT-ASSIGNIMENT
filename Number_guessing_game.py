
def check_guess(guess, secret):
    
    if guess == secret:
        return True
    elif guess > secret:
        print("Please enter a lower number.")
        return False
    else:
        print("Please enter a higher number.")
        return False


secret_number = 7
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number: "))

    # Call the function
    result = check_guess(guess, secret_number)

    # Display the result
    if result == True:
        print("Congratulations! You guessed correctly.")
        print(f"You guessed it in {attempts + 1} attempts.")
        break

    elif result == False:
        attempts += 1

else:
    print("Sorry! You have used all 5 attempts.")
    print(f"The correct number was {secret_number}.")
