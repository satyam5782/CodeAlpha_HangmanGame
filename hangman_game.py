# Project Name: Hangman Game
# importing random module, hangman stages file, and hangman words file
import random
import hangman_stages
import hangman_words

# Introduction and rules of the Hangman game
introduction = "Lets! play HANGMAN game..."
print(introduction.center(50))

rules = """You have to guess the word by entering letters one by one.
If you guessed all letters correctly, you WON the game.
There are only 6 lives, if you guess the wrong word, you lose a life.
Once all your lives get finished, the hangman figure gets completed and you LOSE the game.
"""

# Firstly choose a word randomly from the hangman word file
chosen_word = random.choice(hangman_words.word_list).lower()

# Having 6 chances to guess the letter of the chosen word
lives = 6

# Initialize the display with underscores representing each letter in the chosen word
display = []
for i in range(len(chosen_word)):
    display += '_'
print("The word to be guessed:")
print(display)

# Initialize game_over flag
game_over = False

# Logic behind the game
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    
    # Check if the guessed letter is present in the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    
    # Display the current state of the word
    print(display)
    
    # If the guessed letter is not in the chosen word, decrement lives
    if guessed_letter not in chosen_word:
        lives -= 1
        
        # If lives reach 0, set game_over to True and print a losing message
        if lives == 0:
            game_over = True
            print("\t\t\t\t YOU LOSE!!! \n\t\t\t Better luck next time")
    
    # If no underscores (no words to be guessed) are left in the display, set game_over to True and print a winning message
    if '_' not in display:
        game_over = True
        print("\t\t\t Congratulations!!! YOU WON")
    
    # Display the hangman figure corresponding to the current number of lives
    print(hangman_stages.stages[lives])

# Print the correct word after the game is over
print("The correct word is: ", chosen_word)
