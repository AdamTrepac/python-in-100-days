

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel","trombone"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
blank_char = "_"
char_list = [blank_char] * len(chosen_word)
lives = 6

while True:

    print(stages[lives])

    if blank_char not in char_list:
        print("Congrats, you won!")
        break
    elif lives == 0:
        print("while the ethics of this game are questionable, you have lost")
        break

    guess = input("Please guess a letter in the word: ").lower()

    instances = 0
    index = 0
    for char in chosen_word:
        if char == guess:
            instances += 1
            char_list[index] = char
        index += 1

    if instances == 0:
        lives -= 1

    print("There are", instances, "instances of your letter in the word")
    print(char_list)
    print("")