def is_valid_word(word, letters, required_letter, used_words): #function is defined
  
  if word.upper() == "END": 
    #the word check is bypassed if user enters 'END' - this will allow them to exit the game.
    return True
  for letter in word: #this interates through each letter in the word
    if letter not in letters: 
      '''
      To check if there was a letter in the word that was not
      among the letters allowed to be use( seven letters inputted in previous prompt).
      '''
      print(f'{letter} is not a letter you can use. The only letters you can use are {letters}')
      return False 
      #if invalid letter is found, check is failed and false is returned.
  if len(word)<4:   #To check if the word is at least 4 letters long
    print("Your word must be at least 4 letters long")
    return False 
    #if word is too short, check is failed and false is returned.
  if required_letter not in word:
    #To check if the required letter is present in the word
    print(f'Your word must contain the letter {required_letter}')
    return False 
    #if the required letter is missing, the check is failed and false is returned.
  if word in used_words: #To check if the word has already been used
    print("Already used")
    return False 
    #if the word has already been used then check is failed and false is returned
  return True 
  #If all checks are passed, the word is verified to be valid and true is returned