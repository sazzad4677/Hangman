import random
from hangma_art import stages, logo
from hangman_words import words

print(logo)

lives = 6
chosen_word = random.choice(words)
placeholder = "_" * len(chosen_word)

print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    print(f'********************************************* {lives} / 6 LIVES LEFT ********************************************* ')
    guessed_letters = input("Guess a letter: ").lower()
    if guessed_letters in correct_letters:
        print(f"You guessed the letter: {guessed_letters}")
    
    display = ""
    for letter in chosen_word:
        if letter == guessed_letters:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if guessed_letters not in chosen_word:
        lives -= 1
        print(f"You guessed {guessed_letters}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"********************************************* OOPS, YOU LOST! It was {chosen_word} **********************************************")
    
    if "_" not in display:
        game_over = True
        print("********************************************* Yay, YOU WIN! *********************************************")
        
    print(stages[lives])