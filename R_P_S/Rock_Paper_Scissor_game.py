import random

print("\n Welcome to the Rock, Paper, Scissors Game!\n")
print("'Instructions': \nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("\nPlease choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")



    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice < 1 or choice > 3:
            choice = int(input("Invalid choice. Please enter a number between 1 and 3: "))
    except ValueError:
        print("invalid input. Please enter a number between 1 and 3.")
        continue

    user_choice = choices[choice - 1]

    print(f"\n user Choice: {user_choice}")
    print("Now it's the computer's turn to choose...")

    computer_choice = random.choice(choices)

    print(f"\nComputer Choice: {computer_choice}")


    if user_choice == computer_choice:
        print("\nIt's a tie!")
    elif ((user_choice == "1" and computer_choice == "3") or \
         (user_choice == "2" and computer_choice == "1") or \
        (user_choice == "3" and computer_choice == "2")):
        print("\nYou win!")
    else:
        print("\n Computer wins!")

    # if you want again play the game

    while True:
        play_again = input("\n Do you want to play again? (y/n): ").lower()
        if play_again in ["y", "yes"]:
            break
        elif play_again in ["n", "no"]:
            print("Thanks for playing!")
            exit()
        else:
            print("Please enter 'y' or 'n'.")

    print("\n Let's play again!")

    print()

print("Thanks for playing!")