# This a Hangman Game

# Importing neccessary modules and files 
from dis import dis
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Setting up variables 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
lives = 6
end_of_game = False

# Prints hangman ascii art
print(logo)

# for debugging 
#print(f"Hey the solution is : {chosen_word}")

# Print letter blanks 
for _ in range(word_length):
        display += "_"

# loop until the end of the game is True 
while not end_of_game:

    guess = input("Guess a letter: ").lower()

    # When letter in the chosen word 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    # When user inputs letter that is not in the word 
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word, You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE! ")

    # print display array 
    print(' '.join(display))
    
    #check if all the letter have been guessed right
    if "_" not in display:
        end_of_game = True
        print("You WIN!!")

    # Print hangman image
    print(stages[lives])