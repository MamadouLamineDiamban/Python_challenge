import pandas as pd
import random


dictionary = pd.read_table("./data/mots.txt", header=0, names=['words'])

def word_to_guess(random_word):
    return len(random_word) * "_"


def replace_letter(letter, random_word, word):
        return ''.join([letter if random_word[i] == letter else word[i] for i in range(len(random_word))])


def game():
    random_word_to_guess = random.choice(dictionary['words'])
    print(random_word_to_guess)
    number_attempts = 8
    word = word_to_guess(random_word_to_guess)
    while number_attempts > 0:
        print(word)
        letter = input("Enter a letter: ")[0].lower()
        if letter in random_word_to_guess:
            word = replace_letter(letter, random_word_to_guess, word)
            if word == random_word_to_guess:
                print("Congratulations, you've guessed the word!")
                response = input("Would do you try again ? (yes/no)")
                if response in ('y', 'yes'):
                    game()
                else:
                    break
        else:
            number_attempts -= 1
            print(f"Incorrect! You have {number_attempts} attempts left.")

    if number_attempts == 0: 
        print(f"Sorry, you've run out of attempts. The word was: {word}")
        
        response = input("Would do you try again ? (yes/no)")
        if response in ('y', 'yes'):
            game()

game()


    