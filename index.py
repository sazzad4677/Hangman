import random
from hangma_art import stages, logo
from hangman_words import words

print(logo)

lives = 6
chosenWord = random.choice(words)
placeholder = ""

for _ in range(len(chosenWord)):
    placeholder += "_"

print(placeholder)

gameOver = False

correctLetters = []

while not gameOver:
    print(f'********************************************* {lives} / 6 LIVES LEFT ********************************************* ')
    guessedLetters = input("Guess a letter: ").lower()
    if guessedLetters in correctLetters:
        print(f"You guessed the letter: {guessedLetters}")
    
    display = ""
    for letter in chosenWord:
        if letter == guessedLetters:
            display += letter
            correctLetters.append(letter)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if guessedLetters not in chosenWord:
        lives -= 1
        print(f"You guessed {guessedLetters}, that's not in the word. You lose a life.")
        if lives == 0:
            gameOver = True
            print(f"********************************************* OOPS, YOU LOST! It was {chosenWord} **********************************************")
    
    if "_" not in display:
        gameOver = True
        print("********************************************* Yay, YOU WIN! *********************************************")
        
    print(stages[lives])