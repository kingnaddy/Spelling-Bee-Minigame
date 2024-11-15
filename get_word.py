from valid_word import is_valid_word

def get_word(letters, required_letter, used_words): #function is defined
  word= input("Enter your word: \n") #prompts the user to enter their word
  valid_check=is_valid_word(word,letters, required_letter, used_words)
  ''''
  calls the is_valid_word function and validates the word entered 
  with the criterias entered in the is_valid_word function
  '''

  while valid_check == False: 
    #this makes the function continue prompting the user until a valid word is entered.
    word= input("Enter your word: \n") #asks the user for a new word
    valid_check = is_valid_word(word,letters, required_letter, used_words) 
    #proceeds to validate the new word entered by the user
  return word  
  #once a valid word has been entered, it is returned by the function