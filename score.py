from pangram import is_pangram #DO NOT MODIFY
def get_point_value(word,letters): #function is defined
  x = is_pangram(word,letters) #calls the is_pangram function and checks whether the word is a pangram
  if x == True: 
    print(f'{word} - Pangram!')
    #if the word is a pangram then message is printed to indicate that
    return len(word)+7 #The length of the word with a bonus of seven points is returned as points
  else:
    print(word)
    #if the word is not a pangram then only the word is printed with no message
    return len(word) #only the length of word is returned as points
