# CLASS or CASH: Casino Roulette

import CLASSorCASHConstantsAndStrings
import CLASSorCASHFunctions


def main():
    """
    Run the CLASS or CASH game from Sunday through Saturday.

    Input:
        The player's choices throughout the game.

    Output:
        The player's final balance and whether they won or lost.
    """

    print()
    print(CLASSorCASHConstantsAndStrings.welcome_message)
    print("You are starting with $92,000, the equivalent to one full Holy Cross tuition!")
    print(CLASSorCASHConstantsAndStrings.goal_message)

    money = CLASSorCASHConstantsAndStrings.HC_TUITION

    for current_day in CLASSorCASHConstantsAndStrings.days_of_week:

        print()
        print(f"Today is {current_day}")

        if money >= CLASSorCASHConstantsAndStrings.WINNING_AMOUNT:
            break

        elif current_day == "Sunday":
            CLASSorCASHFunctions.get_schedule(current_day)

        elif money < 1:
            print("You have no money left!")
            print("You must go about your normal day.")
            CLASSorCASHFunctions.get_schedule(current_day)

        else:
            choice = CLASSorCASHFunctions.choose_class_or_cash(current_day)

            if choice == "class":
                CLASSorCASHFunctions.get_schedule(current_day)

            else:
                money = CLASSorCASHFunctions.play_roulette(money)

    print()

    if money >= CLASSorCASHConstantsAndStrings.WINNING_AMOUNT:
        print("Congratulations! You won CLASS or CASH!")
    else:
        print("You lost CLASS or CASH! Better luck next time!")

    print("The week is over, thank you for playing!")
    print(f"Your final amount of money is ${money}")


if __name__ == "__main__":
    main()