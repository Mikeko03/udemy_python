# Imports
import random
from hangman_words import word_list


def play_hangman():
    # Select a word randomly from the word list
    chosen_word = random.choice(word_list)
    
    # Litlle cheat print
    # print(f"Welcome to Hangman! Your chosen word has {len(chosen_word)} letters.\n")

    # Define a function to get a letter from the player
    def get_guess():
        return input("Please enter a letter: ").lower()

    # Initialize variables to keep track of the game state
    guessed_letters = []
    lives = 6
    word_progress = ["_" for _ in chosen_word]

    # Play the game until the player wins or runs out of lives
    while lives > 0 and "_" in word_progress:
        # Get a letter from the player
        guessed_letter = get_guess()

        # Check if the player has already guessed this letter
        if guessed_letter in guessed_letters:
            print(f"You have already guessed {guessed_letter}. Please try a different letter.\n")
        else:
            # Add the guessed letter to the list of guessed letters
            guessed_letters.append(guessed_letter)

            # Check if the guessed letter is in the chosen word
            if guessed_letter in chosen_word:
                for i, letter in enumerate(chosen_word):
                    if letter == guessed_letter:
                        word_progress[i] = letter
            else:
                lives -= 1
                print(f"Sorry, {guessed_letter} is not in the guessed word. You have {lives} lives left.\n")

            # Display the current progress and remaining lives
            print(' '.join(word_progress).upper())
            print(f"You have {lives} lives left.\n___________________________")

    # Check if the player won or lost and print an appropriate message
    if "_" not in word_progress:
        print("\n\n -----------------------\n |Congratulations, you won!|\n -----------------------")
    else:
        print(f"Sorry, you lost. The word was {chosen_word.upper()}.")


# Call the main function to start the game
if __name__ == '__main__':
    play_hangman()
