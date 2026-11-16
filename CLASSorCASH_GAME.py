# CLASS or CASH: Casino Roulette

from CLASSorCASHConstantsAndStrings import HC_TUITION, WINNING_AMOUNT, days_of_week, welcome_message, goal_message
from CLASSorCASHFunctions import get_schedule, choose_class_or_cash, play_roulette


def main():
    """
    Run the CLASS or CASH game from Sunday through Saturday.

    Input:
        The player's choices throughout the game.

    Output:
        The player's final balance and whether they won or lost.
    """

    print()
    print(welcome_message)
    print("You are starting with $92,000, the equivalent to one full Holy Cross tuition!")
    print(goal_message)

    money = HC_TUITION

    for current_day in days_of_week:

        print()
        print(f"Today is {current_day}")

        if money >= WINNING_AMOUNT:
            break

        elif current_day == "Sunday":
            get_schedule(current_day)

        elif money < 1:
            print("You have no money left!")
            print("You must go about your normal day.")
            get_schedule(current_day)

        else:
            choice = choose_class_or_cash(current_day)

            if choice == "class":
                get_schedule(current_day)

            else:
                money = play_roulette(money)

    print()

    if money >= WINNING_AMOUNT:
        print("Congratulations! You won CLASS or CASH!")
    else:
        print("You lost CLASS or CASH! Better luck next time!")

    print("The week is over, thank you for playing!")
    print(f"Your final amount of money is ${money}")


if __name__ == "__main__":
    main()