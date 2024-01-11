import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine", "orange", "pineapple", "raspberry", "strawberry", "tangerine", "watermelon"]
    chosen_word = random.choice(word_list)
    return chosen_word

def hangman(chosen_word):
    word_length = len(chosen_word)
    blanks = []
    guessed = []
    letters_guessed = ''

    for _ in range(word_length):
        blanks.append('_')

    while '_' in blanks:
        print("Word: ", blanks)
        print("Letters Guessed: ", letters_guessed)
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You've already guessed that letter.")
        elif guess in chosen_word:
            index = chosen_word.find(guess)
            while index != -1:
                blanks[index] = guess
                index = chosen_word.find(guess, index + 1)
            guessed.append(guess)
        else:
            guessed.append(guess)
        blanks = ''.join(blanks)
        letters_guessed = ''.join(guessed)

    print("Word: ", blanks)
    print("You win!")

chosen_word = choose_word()
hangman(chosen_word)