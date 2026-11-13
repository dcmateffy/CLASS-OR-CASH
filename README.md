# CLASS or CASH: Casino Roulette


## Game Description

CLASS or CASH is a roulette game in Python where the player must decide between attending class or gambling at the casino.

The game takes place over one full week, beginning on Sunday and ending on Saturday.

The player starts with $92,000, which is roughly equivalent to one full Holy Cross tuition, and the goal is to reach $1,000,000.


## How to Play

1. On Sunday, the player gets to imagine relaxing, doing homework, going to buy groceries for the week, spending time with friends, or preparing for the week ahead.
2. From Monday through Thursday, the player gets to choose between "class" and "cash".
3. Choosing "class" displays the player's schedule for that day.
4. Choosing "cash" takes them to the casino.
5. On Friday and Saturday, the player must gamble if they have money remaining.
6. At the casino, the player chooses an amount to bet between $1 and their current balance.
7. The player can bet on a color (red, black, or green) or a number from 0 to 36.
8. The roulette wheel randomly selects a number and color, determining whether the player wins or loses.
9. The player can gamble for a maximum of three rounds per day, but they can choose to leave the casino earlier.
10. After three rounds, the player automatically leaves the casino and advances to the next day.


## How Betting Works

- Red or Black: Win 1x the amount bet.
- Green: Win 35x the amount bet.
- Correct Number: Win 100x the amount bet.
- Incorrect Bet: Lose the amount bet.

After each spin, the player can choose to gamble again or leave the casino and advance to the next day, unless they have already played three rounds that day.

If the player runs out of money, they cannot gamble anymore.

The game ends after Saturday or when the player reaches $1,000,000. The player wins by reaching $1,000,000 and loses if they finish the week without reaching that goal.


## Tracking the Player's State

The player's state is primarily represented by the variable "money", which stores their current balance throughout the game.

The variable starts at $92,000 and changes depending on whether the player wins or loses a bet.

The player's current balance is passed into the play_roulette() function, where update_money() calculates and returns the new balance after each spin.

The updated balance is then returned to the main program, allowing the player's money to carry over from one day to the next.

I chose to represent the player's state using a variable because it is a simple way to track their progress throughout the game.

It also makes it easier to determine whether the player has enough money to continue gambling, has run out of money, or has reached the $1,000,000 goal.

The game also uses "current_day" to track the player's progress through the week, "play_again" to determine whether they want to continue gambling, and "rounds_played" to track the number of roulette rounds played each day.

The "rounds_played" variable starts at zero each time the player enters the casino and increases by one after each spin. Once it reaches three, the player must leave the casino for that day.

I also added a check_game_status() function that uses the player's current balance to determine whether they have won, run out of money, or can continue playing. The play_roulette() function calls this function after each spin to check the player's status.


## Control Flow

The game uses a for loop to move through each day of the week. If the player chooses "class", their schedule is displayed. If they choose "cash", they gamble at the casino. A while loop allows the player to gamble up to three times per day. The game ends when the player reaches $1,000,000 or finishes Saturday.


## Code Organization

The project is organized into three Python files:

- CLASSorCASH_GAME.py: Runs the main game and tracks the player's progress throughout the week.
- CLASSorCASHFunctions.py: Contains the functions used for choosing class or cash, displaying schedules, placing bets, spinning the roulette wheel, updating the player's balance, and checking the player's status.
- CLASSorCASHConstantsAndStrings.py: Stores the constants, lists, and messages used throughout the game.

Separating the code into different files makes the project easier to read, organize, and understand.


## Improvements Based on Peer Feedback

After receiving feedback from my two peer reviewers, I made several changes to improve the organization and gameplay.

First, I separated my original code into three Python files instead of keeping everything in one file. I also updated the docstrings for my functions to better explain what each function does, its inputs, and its outputs.

I improved the input validation for betting amounts and roulette numbers so that the game can handle invalid inputs, such as entering letters instead of numbers, without crashing.

I also added a limit of three roulette rounds per day. Previously, the player could continue gambling as many times as they wanted during a single day. This change prevents the player from gambling indefinitely and helps the game progress through the entire week.

I also added a function to check whether the player has won, lost all their money, or can continue playing. This helps organize the code and makes it easier to track the player's progress.

Overall, these changes make the game more organized, easier to understand, and more enjoyable to play.