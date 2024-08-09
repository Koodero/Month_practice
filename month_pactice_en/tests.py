import random
import os

# Function to clear the terminal screen
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

# This function asks the user if they want to continue playing or not
def want_to_continue(points: int, attempts: int):
    print(f"Your score so far is {points}/{attempts}\n")
    print("Do you want to continue with this exercise?")
    
    answer = input("(Yes / No): ").strip().lower()
    clear_screen()

    return answer in ["yes", "y"]

# This is the user's first option: The user is given a month, and they need to respond with the month's order number
def month_number(dictionary: dict):
    points = 0
    attempts = 0
    
    while True:
        # Generate a random month for the user to guess
        month_num = random.randint(1, 12)

        print("Which number month is this?")
        print(dictionary[month_num], "\n")
        
        answer = input("Enter a number between 1 and 12: ").strip()

        # Check if the user's answer is valid
        if not answer.isdigit() or not (1 <= int(answer) <= 12):
            print("Invalid input. Please enter a number between 1 and 12.")
            continue

        clear_screen()

        # Check if the user's answer is correct or not
        answer_sentence = f"{dictionary[month_num]} is the {month_num} month of the year"
        if answer == str(month_num):
            print(f"Correct, {answer_sentence}!")
            points += 1
        else:
            print(f"Wrong, {answer_sentence} :(")
            print(f"You answered: {answer.title()}.")
        attempts += 1

        # Ask if the user wants to continue
        if not want_to_continue(points, attempts):
            break
        
    return points, attempts


# This is the user's second option: The user is given a month's order number and needs to respond with the corresponding month
# Same steps as month_number()
def number_month(dictionary: dict):
    points = 0
    attempts = 0

    while True:
        month_num = random.randint(1, 12)

        print("Which month corresponds to the following number?")
        print(str(month_num) + ":\n")

        answer = input("Enter the month here: ").strip()

        clear_screen()

        answer_sentence = f"{dictionary[month_num]} is the {month_num} month of the year"

        if answer.title() == dictionary[month_num]:
            print(f"Correct, {answer_sentence}!")
            points += 1
        else:
            print(f"Wrong, {answer_sentence} :(")
            print(f"You answered: {answer.title()}.")
        attempts += 1

        if not want_to_continue(points, attempts):
            break
        
    return points, attempts


# This is the user's third option: The user is given a month's order number in the form of a clock, and they need to respond with the corresponding month
# Same steps as month_number()
def clock_number(month_dict: dict, clock_dict: dict):
    points = 0
    attempts = 0

    while True:
        month_num = random.randint(1, 12)

        print("Which month does the clock's hand correspond to?")
        print(clock_dict[month_num], "\n")

        answer = input("Enter the month corresponding to the number here: ").strip()

        clear_screen()

        answer_sentence = f"{month_dict[month_num]} is the {month_num} month of the year"

        if answer.title() == month_dict[month_num]:
            print(f"Correct, {answer_sentence}!")
            points += 1
        else:
            print(f"Wrong, {answer_sentence} :(")
            print(f"You answered: {answer.title()}.")
        attempts += 1

        if not want_to_continue(points, attempts):
            break
        
    return points, attempts
