def is_pangram(guess, letters): #function is defined
  check = True
   #check is initialized as true but it can be changed based on conditions.
  for letter in letters: 
    #this iterates through each letter that was inputted by the user when asked for seven letters
    if letter not in guess: 
      #this checks if any of the letters is not present in the guessed word 
      check = False 
      #If a letter is missing, check is changed to False

  return check
  #if all the letters are present then the word is a pangram and True is returned, otherwise False is returned