import random

while True:

    number_to_guess = random.randint(1, 10)
    while True:
        user_guess = input("Guess a number between 1 and 10: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Try again.")
            continue
        if int(user_guess) > 10 or int(user_guess) < 1:
            print("Number is out of range")
            continue
        if user_guess == number_to_guess:
            print("You guessed right!")
            break
        else:
            print("You guessed wrong. Try again.")
            continue

    keep_playing = input("Do you want to play again? (y/n): ")
    if keep_playing.lower() != "y":
        print("Thank you for playing")
        break