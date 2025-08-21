import random

def game():
    go=0
    print("I will think about a random number between 1 and 100 and you have to guess it!")
    lvl= input("Choose a difficulty level (1,2,3): ")
    if lvl == '1':
        print("You have 10 attempts to guess the number.")
        tries= 10
    elif lvl == '2':
        print("You have 7 attempts to guess the number.")
        tries = 7
    elif lvl == '3':
        print("You have 5 attempts to guess the number.")
        tries = 5
    else:
        print("Invalid level selected. Defaulting to level 1.")
        print("You have 10 attempts to guess the number.")
        tries = 10


    n= random.randint(1, 100)
    guess = 0  
    while guess != n and go<=tries:
        guess = int(input("Enter your guess: "))
        go += 1
        if guess < n:
            print("Too low! Try again.")
        elif guess > n:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
    if go >= tries:
        print("Sorry, you've used all your attempts. The number was:", n)
    print("Game over!")

run=0
repeats = int(input("How many times do you want to play the game? "))
while run < repeats:
    game()
    run += 1
    if run < repeats:
        print("Starting a new game...")
    else:
        print("Thanks for playing! Goodbye!")
        break
    print("\n")  # Adding a newline for better readability between games