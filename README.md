Noble's Spelling Bee Game 🎯🐝

Welcome to Noble's Spelling Bee, an interactive and fun word-guessing game where players score points by forming valid words from a set of seven letters. 
Sharpen your spelling skills while aiming for the highest score!

Features

-Input 7 uppercase letters to form your game set.

-Choose a required letter that must appear in all guessed words.

-Guess as many valid words as possible.

-Track your score dynamically.

-End the game anytime by entering END, and view your final score







Getting Started


Prerequisites
Python 3.x installed on your system.




Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/YourUsername/SpellingBee.git



Navigate to the project folder:
bash
Copy code
cd SpellingBee


Ensure the following external modules are available in your project:
get_word: Provides user input for guessed words.
get_point_value: Calculates the score for each valid word.


Run the game:
bash
Copy code
python spelling_bee.py



Playing the Game

-Start the game: Enter 7 distinct uppercase letters separated by commas (e.g., A,B,C,D,E,F,G).

-Choose the required letter: Select one letter from your set that will be mandatory in all your words.

-Guess words: Enter words that use only the 7 provided letters, ensuring the required letter is included.

-Stop the game: When you're done, type END to see your total score.




Example Gameplay





Welcome to Noble's Spelling Bee!

*USE UPPERCASE THROUGHOUT*

Enter your seven letters then guess words

Guess as many valid words to gather lots of points

Anytime you can't think of more words - Enter 'END'

Your Score will pop up in the end! Enjoy!






Enter your 7 letters, separated by commas: A,B,C,D,E,F,G

Which of these 7 letters ['A', 'B', 'C', 'D', 'E', 'F', 'G'] will be your required letter? A

Enter a word using the letters: FACE

Enter a word using the letters: BREAD

Enter a word using the letters: END

Your final score is 24








Functions Overview

play_spelling_bee()

Manages the game flow, including user input, word validation, and score calculation.

check_letters(letters)

Validates that the input consists of exactly 7 unique, uppercase letters.







External Dependencies

get_word: Prompts and retrieves valid words from the player.

get_point_value: Computes the point value for each valid word.







Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the game.







License

This project is open-source and available under the MIT License.






Contact

For any questions or feedback, feel free to reach out to Noble Adike @nobleadike@gmail.com.

Replace YourUsername in the repository URL with your GitHub username, and ensure all mentioned modules are included or documented appropriately.


