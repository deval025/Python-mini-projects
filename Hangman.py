import random as rand
import string
from words import words

def getValidWord (words):
    # Generates a word from the list of words in the word.py file 
    word=rand.choice(words)
    while '_' in word or ' ' in word :
        word = rand.choice(words)
    return word.upper()
def hangman():
    word = getValidWord(words) 
    word_letters = set(word) # Stores the distinct letters in the word
    alphabet = set(string.ascii_uppercase)# Set of all Upper case letters
    used_letters= set()# Empty set to keep track of the letters user entered
    
    lives = 6

    # Getting User Input
    while len(word_letters)>0 and lives > 0:
        # Printing the letters user has already guessed 
        print(f"you have {lives} lives.\n you have already used these letters:", " ".join(used_letters))
        
        # Printing the gussed words (i.e W_RD)
        #the below for loop is shoterned by using list comprehension 
        """for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('_')
        print(' '.join(word_list))"""

        word_list= [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_input= input("guess a letter: ").upper()
        if user_input in alphabet - used_letters:    # Checks if the letter is valid and not yet gussed
            used_letters.add(user_input)
            if user_input in word_letters :          # Checks if the letter is in the random genetated Word
                word_letters.remove(user_input)
            else:
                lives = lives-1
                print("letter is not in the word")
        
        elif user_input in used_letters:             # Checks for repeating words
            print("you alredy tried that letter. Please try another letter")
        
        else:                                        # Checks for invalid Characters
            print("The character you entered is Invalid")    
    if lives == 0:
        print("Sorry! you died. The word was: ", ' '.join(word))
    else:
        Print("Congrats you won the word is: ", " ".join(word))
hangman()