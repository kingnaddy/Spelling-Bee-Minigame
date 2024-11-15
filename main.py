# DO NOT REMOVE
from get_word import get_word              
from score import get_point_value 

def play_spelling_bee():
  print("Welcome to Noble's Spelling Bee!\n*USE UPPERCASE THROUGHOUT* \nEnter your seven letters then guess words \nGuess as many valid words to gather lots of points \nAnytime you can't think of more words - Enter 'END' \nYour Score will pop up in the end! \n Enjoy! ")
  letters=input("Welcome to Spelling Bee! Enter your 7 letters, separated by commas:")
  #welcomes and prompts the user to enter 7 letters separated by commas.
  letters=letters.split(",") 
  #the input of letters is split into a list with comma as the seperator

  #The loop below ensures the user enters exactly 7 valid letters and it continues until the user does so
  while not check_letters(letters):
    print("Please enter valid input, You should enter seven letters in uppercase seperated by commas(,)")
    letters = input("Enter your 7 letters, separated by commas (e.g., A,B,C,D,E,F,G): ").split(",")

  

  required_letter = input(f'Which of these 7 letters {letters} will be your required letter?')

  #This prompts the user to choose a required letter from the entered letters
  while required_letter not in letters: #This is to ensure the chosen letter is among the entered letters
    print(f'{required_letter} is not an available letter. Please choose from the following: {letters}')
    required_letter = input(f'Which of these 7 letters {letters} will be your required letter?')

  #A list is created to keep track of words that have already been used.
  used_words= [] 
  score = 0 #Score is initialized to 0
  word = get_word(letters, required_letter, used_words)
  #get_word function is called to get first word from user

  #Game is looped until the user enters "END".
  while word != "END":
    used_words.append(word) #This adds the word to the list of used words
    score += get_point_value(word,letters)
    #get_point_value function called to update the score based on the word's point value.
    word = get_word(letters, required_letter, used_words) #get_word function called to get the next word.

  # Once the user enters "END", the final score is printed.
  if word == "END":
    print(f'Your final score is {score}')


def check_letters(letters):
    
    #if the number of letters is not equal to seven then return false
    if len(letters) != 7:
        return False
    
    # Each letter for validity is checked: it should be a single, uppercase and alphabetic character
    for letter in letters:
        if len(letter) != 1:
            return False
        if not letter.isupper():
            return False
        if not letter.isalpha():
            return False

    #Make sure there are no duplicates by comparing the length of the list with the set 
    if len(set(letters)) != 7:
        return False
    
    return True


  
#function is called to start the game.
play_spelling_bee() # DO NOT REMOVE'
