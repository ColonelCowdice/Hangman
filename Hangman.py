# Welcome To Zion's Hangman Code

# Imports

import random

# Import hangman.txt and get a random word
def Newword():
    with open("hangman.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

        # print random string
        word = (random.choice(words))
        return word.upper()


# Import Graphics

from Graphics import *

# Play

def play(word):
    wordfinished = "_" * len(word)

    #Guessed Letters and Words list

    GuessedCharacters = []
    GuessedWords = []

    # Tries (6 cause the average word len is 4.7 but I'll give an extra cause people are dumb :) )

    Guesses = 6

    # Did player get the word right True/False

    guessed = False

    #Check if word/letter already been guessed

    TryedAlready = False

    # Front-end Code lame (Welcome and Start)

    print("Welcome to Zion's Hangman")
    print("Here are the rules https://www.youtube.com/watch?v=cGOeiQfjYPk\n")
    print(Graphics(Guesses))
    print(wordfinished)

    # Playing

    # Check if you can Play loop

    while not TryedAlready and Guesses > 0:

        # Input (Choose a letter or character)

            # Show user what letters or words they've already guessed
            print("\nThese are the letters you've guessed")
            print(GuessedCharacters)
            print("\nThese are the words you've guessed")
            print(GuessedWords)

            guess = input("\nGuess a character or a word: ").upper()

            # If guess length is a letter long, and is alpha then check if its already been used before proceeding

            if len(guess) == 1 and guess.isalpha():
                if guess in GuessedCharacters:
                    print("You already guessed the letter", guess)

            # If guess (letter) is not in the word then take away a try

                elif guess not in word:
                    print(guess, "is not in the word.")
                    Guesses -= 1

                    # Add to guessed letters

                    GuessedCharacters.append(guess)

            # If guess (letter) is in the word

                else:
                    print("Good job,", guess, "is in the word!")

                    # Add to guessed letters

                    GuessedCharacters.append(guess)

                    # Replacing the blank spot with guessed letter

                    Replace = list(wordfinished)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        Replace[index] = guess
                    wordfinished = "".join(Replace)

                    # Check if there is anymore blank spaces in the word bar, if not then you win!

                    if "_" not in wordfinished:
                        guessed = True

            # If you've already guessed that word

            elif len(guess) == len(word) and guess.isalpha():
                if guess in GuessedWords:
                    print("You already guessed the word", guess)

                # If not and still wrong, remove a try

                elif guess != word:
                    print(guess, "is not the word.")
                    Guesses -= 1
                    GuessedWords.append(guess)

                # If somehow you got it right

                else:
                    guessed = True
                    wordfinished = word

            # If guess is not a word or a letter

            else:
                print("Not a valid guess.")
            print(Graphics(Guesses))
            print(wordfinished)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

# Simple play again code that I copied and pasted from github
def main():
    word = Newword()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = Newword()
        play(word)


if __name__ == "__main__":
    main()


