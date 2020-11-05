secret = 5
guess = int(input("Guess the secret number: "))

if guess == secret:
    print("Congratulations! It is number 5!")

else:
    print("Close but WRONG. Better luck next time! The secret number is not " + str(guess))