from tests import month_number, number_month, clock_number, clear_screen
from big_things import clocks, month_dictionary, start_options
from score_class import Scores

# Main menu where the user is given instructions and shown their own scores.
def main():
    clear_screen()

    # Create a player variable from the Scores class to easily store the scores
    player = Scores()

    while True:

        # Check if the user has already done any exercises, if so, show their scores
        if player.attempts != 0:
            print(f"Your score so far is {player.points}/{player.attempts}")
            print(f"You have answered approximately {(player.points / player.attempts) * 100:.0f}% of the questions correctly\n\n")

        # Show the user the program's different options and get their choice
        print(start_options)
        user_choice = input("Choose one of the given options: ").strip()
        clear_screen()

        # Depending on the user's choice, start an exercise or exit the loop and end the game
        if user_choice == "1":
            points, attempts = month_number(month_dictionary)

        elif user_choice == "2":
            points, attempts = number_month(month_dictionary)

        elif user_choice == "3":
            points, attempts = clock_number(month_dictionary, clocks)

        elif user_choice == "4":
            break
        
        # If an invalid choice is given, offer the user to choose again
        else:
            clear_screen()
            print("!!!! Try again, please choose a valid option !!!!\n")

        # Update the player's scores, reset points and attempts to zero in case of an invalid answer
        player.add_points(points=points, attempts=attempts)
        points = attempts = 0


# This runs after the break - choosing option 4 to end the game
    clear_screen()
    try:
        print(f"Your final score was {player.points} / {player.attempts}.")
        print(f"You answered approximately {(player.points / player.attempts) * 100:.0f}% of the questions correctly\n\n")
    except ZeroDivisionError:  # Avoid division by zero if both points and attempts are 0
        print("You didn't even try 😂")
    print("Thanks for playing !!!")


if __name__ == "__main__":
    main()
