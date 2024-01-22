import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

chosen_word = random.choice(hangman_words.word_list)
blank_char = "_"
char_list = [blank_char] * len(chosen_word)
guessed_chars = []
lives = 6

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

while True:

    print(hangman_art.stages[lives])

    if blank_char not in char_list:
        print("Congrats, you won!")
        break
    elif lives == 0:
        print("while the ethics of this game are questionable, you have lost")
        break

    guess = input("Please guess a letter in the word: ").lower()
    
    if guess in guessed_chars:
        print(guess, "has already been guessed")
    else:
        guessed_chars += guess

        instances = 0
        index = 0
        for char in chosen_word:
            if char == guess:
                instances += 1
                char_list[index] = char
            index += 1

        if instances == 0:
            lives -= 1

        print("There are", instances, "instances of", guess, "in the word")
    print(f"{' '.join(char_list)}")
    print("")