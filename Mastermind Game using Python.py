import random 


secret_num = random.randrange(1000,10000)

print("\n Welcome to Mastermind!")
print("Try to guess the 4-digit number.\n")

print(secret_num)


attempts = 0


while True:
    try:
        guess = int(input("Enter Your Four digit guess Number: "))
        if guess < 1000 or guess > 9999:
            print("Please Enter a valid 4-digit number")
            continue
    except ValueError:
        print("Invalid input. Please enter a 4-digit number.")
        continue

    attempts += 1 

    if guess == secret_num:
        print("\n Congulations You've become a Mastermind!")
        print(f"You guessed the number in {attempts} attempts.")
        break

    guess_str = str(guess)
    secret_str = str(secret_num)

    count = 0

    how_many_numbers_correct = ""


    for index , i in enumerate(secret_str):
       if i != guess_str[index]:
            print(f"\n Not quite the number.")
            print(f"You got {count} digit(s) correct.\n")
            break
       else :
            count += 1
            if count == 1:
                how_many_numbers_correct = "First digit is Correct"
            elif count == 2:
                how_many_numbers_correct = "First two digits are Correct"
            elif count == 3:
                how_many_numbers_correct = "First three digits are Correct"
            elif count == 4:    
                how_many_numbers_correct = "All four digits are Correct"


    print(f"\n Not quite the number.")
    print(f"You got {count} digit(s) correct.\n")
    print(f"{how_many_numbers_correct}\n")

















