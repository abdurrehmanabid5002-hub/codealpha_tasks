import random


def hangman_game():
    words = ["apple", "python", "computer", "orange", "school"]
    sceret_word = random.choice(words)
    attempts = 6
    guessed_letters = []

    while attempts > 0:

        print("\nWord: ", end="")
        word_complete = True

        for letters in sceret_word:
            if letters in guessed_letters:
                print(letters, end=" ")
            else:
                print("_", end=" ")
                word_complete = False
        print()

        if word_complete:
            print("Congratulations you win")
            break

        guess = input("enter your letter to guess:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter only one allphabet letter")
            continue

        if guess in guessed_letters:
            print("you already guesse this letter")
            continue

        guessed_letters.append(guess)

        if guess in sceret_word:
            print("correct")
        else:
            attempts -= 1
            print("Wrong")
            print(f"remaining guesses: {attempts}")

    if attempts == 0:
        print("All the attempts are gone you lost")
        print(f"The word was: {sceret_word}")


hangman_game()
