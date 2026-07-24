import random

def play_hangman():
    words = ["python", "engineer", "software", "keyboard", "monitor"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses_left = 6

    print("Welcome to Hangman!")
    print("I have selected a word. Let see if you can guess it.")

    while incorrect_guesses_left > 0:
        current_display = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                current_display += letter
            else:
                current_display += "_"
        
        print(f"\nWord: {current_display}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        
        if "_" not in current_display:
            print(f"\nCongratulations! You guessed the word '{word_to_guess}' correctly. Well done!")
            return

        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("That input isn't valid. Please make sure to enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already tried that letter. Let's try a different one.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_guesses_left -= 1
            print(f"Ah, sorry. The letter '{guess}' is not in the word.")
        else:
            print(f"Great guess! The letter '{guess}' is in the word.")

    print(f"\nGame over! You have run out of guesses. The word I was thinking of was '{word_to_guess}'.")

if __name__ == "__main__":
    play_hangman()