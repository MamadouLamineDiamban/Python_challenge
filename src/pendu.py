import pandas as pd
import random

# Load the dictionary of words
dictionary = pd.read_table("./data/mots.txt", header=0, names=['words'])

# Generate a masked word with underscores
def word_to_guess(word):
    return "_" * len(word)

# Replace letters in the masked word if they are found in the random word
def replace_letter(letter, random_word, current_word):
    return ''.join(
        [letter if random_word[i] == letter else current_word[i] for i in range(len(random_word))]
    )

# Main game function
def game():
    # Choose a random word from the dictionary
    random_word_to_guess = random.choice(dictionary['words'])
    print(f"Word to guess (debug): {random_word_to_guess}")  # Debug, can be removed in production
    
    number_attempts = 8  # Set the number of attempts
    guessed_word = word_to_guess(random_word_to_guess)  # Initialize the masked word
    
    # Game loop
    while number_attempts > 0:
        print(guessed_word)
        letter = input("Enter a letter: ")[0].lower()  # Take a letter from user input
        
        if letter in random_word_to_guess:
            # Update the guessed word if the letter is in the random word
            guessed_word = replace_letter(letter, random_word_to_guess, guessed_word)
            if guessed_word == random_word_to_guess:
                # If the player guesses the word, congratulate and ask if they want to replay
                print("Congratulations, you've guessed the word!")
                if replay():
                    game()
                return
        else:
            # Reduce the number of attempts if the guess was incorrect
            number_attempts -= 1
            print(f"Incorrect! You have {number_attempts} attempts left.")

    # If attempts are exhausted, reveal the word and ask if they want to replay
    print(f"Sorry, you've run out of attempts. The word was: {random_word_to_guess}")
    if replay():
        game()

# Ask if the player wants to play again
def replay():
    response = input("Would you like to try again? (yes/no): ").strip().lower()
    return response in ('y', 'yes')

    
# Game initialization
if __name__ == "__main__":
    print("Welcome to the Word Guessing Game!")
    game()
