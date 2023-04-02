# Name                 : Deshmukh, Dhiraj Subhash
# Matriculation Number : 3147051

# Number Guess Game Program
# Purpose: to generate a random integer number between 1 and 100 and ask user to guess it. Also,
# to give user a feedback on the guesses. Moreover, to count the number of user's guesses it took to find the
# correct answer.


import random                   # library to generate random numbers
import time                     # library to add waiting time functionality
from pygame import init         # library to assist sound effects
from pygame.mixer import Sound  # specific function in pygame library for sound effects

# Initialize pygame
init()
# Load the sound effect and assign to variables
correct = Sound("correct.mp3")
wrong   = Sound("wrong.mp3")
quit   = Sound("quit.mp3")


# Function to generate random integers between 1 and 100
def generate_random_number():
    random_number = random.randint(1, 100)
    return random_number

# Function to start the game
def play_game():
    # Call the random number initialisation function
    random_number = generate_random_number()
    # Initialise the number of guesses counter
    num_guesses = 0

    # While loop to check the user guess and to give feedback on it
    while True:
        # try until any invalid input, such as strings and floats.
        try:
            # store the user input in integer form
            user_guess = int(input("Guess a number between 1 and 100 (enter 0 to quit!): "))
            # increment the number of guesses counter
            num_guesses += 1
            # Feedback for the guess less than the answer, (except 0, 0 is to quit the game)
            if user_guess < random_number and user_guess != 0:
                print("Too low!")
                # Play the sound effect for wrong guess
                wrong.play()
            # Feedback for the guess greater than the answer
            elif user_guess > random_number:
                print("Too high!")
                # Play the sound effect for wrong guess
                wrong.play()
            # Condition to quit the game with a print statement
            elif user_guess == 0:
                print("Thank you! The number was "+str(random_number)+".")
                # Play the sound effect
                quit.play()
                # waiting time 4 sec to let the sound play
                time.sleep(4)
                # break the while loop
                break
            # Condition for correct guess with a print statement and number of guesses
            else:
                # Play the sound effect
                correct.play()
                print("Congratulations! You guessed the number in " + str(num_guesses) + " guesses.")
                # waiting time 7 sec to let the sound play
                time.sleep(7)
                # break the while loop
                break
        # Throw an error for invalid inputs, such as floats and strings
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            # continue the program and let user enter a valid input
            continue

# To run/start the game by calling this function
play_game()
