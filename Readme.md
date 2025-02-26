# Hangman Game

A simple command-line Hangman game written in Python.

## Description

This Hangman game randomly selects a word from a predefined list and challenges the player to guess it letter by letter. The player starts with 6 lives and loses one for each incorrect guess. The game ends when the player either correctly guesses the word or runs out of lives.

## Features

- Random word selection from a predefined list.
- A visual representation of the Hangman stages.
- Input validation to prevent repeated guesses.
- Clear display of game progress and remaining lives.

## Requirements

- Python 3.x

## Setup and Installation

1. Clone this repository or download the script.
2. Ensure you have Python installed on your system.
3. Install required dependencies (if any).
4. Run the script:
   ```sh
   python hangman.py
   ```

## Files

- `hangman.py`: The main script that runs the game.
- `hangma_art.py`: Contains ASCII art for Hangman stages and the logo.
- `hangman_words.py`: Contains the list of words for the game.

## How to Play

1. The game displays a blank word represented by underscores (`_ _ _ _`).
2. You guess one letter at a time.
3. If the letter is in the word, it will be revealed in its correct position.
4. If the letter is not in the word, you lose a life.
5. The game continues until you guess the word correctly or run out of lives.

## Example Gameplay

```
Welcome to Hangman!
_ _ _ _ _
Guess a letter: a
_ a _ _ a
Guess a letter: b
You guessed b, that's not in the word. You lose a life.
5/6 LIVES LEFT
```

## License

This project is for educational purposes and is free to use and modify.

## Contributions

Feel free to submit issues or contribute to improving the game!

