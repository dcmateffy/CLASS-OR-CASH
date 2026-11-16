# CLASS or CASH Functions

import random
from CLASSorCASHConstantsAndStrings import activities, red_numbers, messages, WINNING_AMOUNT


def choose_class_or_cash(day):
    """
    Ask the player to choose class or cash for the current day.

    Input:
        day: The current day of the week.

    Output:
        The player's choice of "class" or "cash".
    """

    if day == "Friday" or day == "Saturday":
        print("Today you MUST choose CASH!")
        choice = "cash"

    else:
        choice = input("Choose class or cash: ").lower()

        while choice != "class" and choice != "cash":
            choice = input("Please enter class or cash: ").lower()

    return choice


def get_schedule(day):
    """
    Display the player's schedule or a random Sunday activity.

    Input:
        day: The current day of the week.

    Output:
        Prints the player's schedule or Sunday activity.
    """

    if day == "Sunday":
        activity = random.choice(activities)

        print(activity)
        print("Hope you feel ready for the busy week ahead!")

    elif day == "Monday" or day == "Wednesday":
        print("You have Intro Python at 10am, Methods of Numerical Analysis at 1pm, and practice in the afternoon/evening!")

    elif day == "Tuesday" or day == "Thursday":
        print("You have Environmental Perspectives at 9:30am, Probability Theory at 11am, and practice in the afternoon/evening!")

    else:
        print("Enjoy your day off!")

    print("Have fun!")



def get_bet(money):
    """
    Ask the player how much money they want to bet.

    Input:
        money: The player's current balance.

    Output:
        A valid bet amount between $1 and the player's balance.
    """

    while True:
        try:
            bet_amount = int(input("How much would you like to bet? $"))

            if bet_amount >= 1 and bet_amount <= money:
                return bet_amount

            else:
                print("Invalid bet, you must bet somewhere between $1 and your current total!")

        except ValueError:
            print("Please enter a valid number!")


def choose_bet_type():
    """
    Ask the player whether they want to bet on color or number.

    Input:
        The player enters "color" or "number".

    Output:
        The player's choice of "color" or "number".
    """

    print("Bet on color (1x multiplier, 35x for green) or number (100x multiplier).")
    bet_type = input("Would you like to bet on color or number? ").lower()

    while bet_type != "color" and bet_type != "number":
        bet_type = input("Please enter color or number: ").lower()

    return bet_type


def choose_bet_color():
    """
    Ask the player which roulette color they want to bet on.

    Input:
        The player enters "red" or "black" or "green".

    Output:
        The player's choice of "red" or "black" or "green".
    """

    bet_color = input("Choose red, black, or green: ").lower()

    while bet_color != "red" and bet_color != "black" and bet_color != "green":
        bet_color = input("Please enter red, black, or green: ").lower()

    return bet_color


def choose_bet_number():
    """
    Ask the player which roulette number they want to bet on.

    Input:
        The player enters a number between 0 and 36.

    Output:
        The player's chosen roulette number.
    """

    while True:
        try:
            bet_number = int(input("Choose a number from 0 to 36: "))

            if bet_number >= 0 and bet_number <= 36:
                return bet_number

            else:
                print("Please choose a number from 0 to 36!")

        except ValueError:
            print("Please enter a valid number!")


def spin_wheel():
    """
    Randomly spin the roulette wheel and determine the result.

    Input:
        None.

    Output:
        The randomly selected number and its corresponding color.
    """

    spin_number = random.randint(0, 36)

    if spin_number == 0:
        spin_color = "green"

    elif spin_number in red_numbers:
        spin_color = "red"

    else:
        spin_color = "black"

    return spin_number, spin_color


def random_prespin_message():
    """
    Randomly select and print a message before spinning the wheel.

    Input:
        None.

    Output:
        Prints a randomly selected message.
    """ 

    message = random.choice(messages)

    print(message)


def update_money(money, bet_amount, bet_type, bet_choice, spin_number, spin_color):
    """
    Determine whether the player won or lost and update their balance.

    Inputs:
        money: The player's current balance.
        bet_amount: The amount of money the player bet.
        bet_type: Whether the player bet on color or number.
        bet_choice: The color or number the player selected.
        spin_number: The number the roulette wheel landed on.
        spin_color: The color the roulette wheel landed on.

    Output:
        The player's updated balance after the bet.
    """

    if bet_type == "color":

        if bet_choice == spin_color:

            if bet_choice == "green":
                money = money + 35 * bet_amount

            else:
                money = money + bet_amount

            print("You won!")

        else:
            money = money - bet_amount
            print("You lost!")

    else:

        if bet_choice == spin_number:
            money = money + (100 * bet_amount)
            print("You won!")

        else:
            money = money - bet_amount
            print("You lost!")

    return money



def check_game_status(money):
    """
    Check whether the player has won, lost, or can continue playing.

    Input:
        money: The player's current balance.

    Output:
        "won", "lost", or "playing" based on the player's balance.
    """

    if money >= WINNING_AMOUNT:
        return "won"

    elif money < 1:
        return "lost"

    else:
        return "playing"


def play_roulette(money):
    """
    Allow the player to gamble for up to 3 rounds per day.

    Input:
        money: The player's current balance.

    Output:
        The player's updated balance after leaving the casino.
    """

    play_again = "yes"
    rounds_played = 0

    while play_again == "yes" and money >= 1 and money < WINNING_AMOUNT and rounds_played < 3:

        print()
        print(f"You have ${money}")

        bet_amount = get_bet(money)
        bet_type = choose_bet_type()

        if bet_type == "color":
            bet_choice = choose_bet_color()
        else:
            bet_choice = choose_bet_number()

        random_prespin_message()
        print("The wheel is spinning...")

        spin_number, spin_color = spin_wheel()

        print(f"The ball landed on {spin_number}, {spin_color}")

        money = update_money(money, bet_amount, bet_type, bet_choice, spin_number, spin_color)

        rounds_played = rounds_played + 1

        print(f"You now have ${money}")

        
        status = check_game_status(money)

        if status == "won":
            print("Congratulations! You reached $1,000,000!")

        elif status == "lost":
            print("You ran out of money, sorry!")
            print("You cannot gamble for the rest of the week!")

        elif rounds_played == 3:
            print("You have reached the maximum of 3 rounds for today!")
            print("You must leave the casino and continue to the next day.")

        else:
            play_again = input("Play again? (yes/no): ").lower()

            while play_again != "yes" and play_again != "no":
                play_again = input("Please enter yes or no: ").lower()

    return money