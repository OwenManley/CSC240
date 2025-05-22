# -*- coding: utf-8 -*-
"""
-Owen Manley, CSC 240, Assignment #3.-
This assignment creates a game that adds gibberish to inputted words; thus,
making a normal word turn into a gibberish word.
"""
def add_gibberish(syllable1, syllable2, word):
#This function is used to add gibberish to the word the user wants
#to translate.
   vowels = 'aeiouAEIOU' #Vowels used for later.
   translated_word = '' #Empty string for the final word that's translated.
   
   #Entire process for adding gibberish to vowels.
   for i in word: #Iterating through the inputted word.
       if i.lower() in vowels: #If the word has a vowel.
       #Nested if for if there is a "*" in the index '0'.
           if syllable1[0] == ('*'): 
               #When the word is finally translated, replace "*" with
               #original vowel. Replace is a built-in system used to replace 
               #values.
               translated_word += syllable1.replace('*', i)
           else:
               #Add the syllable to the final translated word.
               translated_word += syllable1
               #Make this apply to the second syllable too.
               syllable1 = syllable2
       else:
           #Add the syllables to the original word to be translated. Which 
           #is then added to translated_word.
           translated_word += i
   
    #Return the new word.
   return translated_word

def word_translator (word):
    #User enters input for first and second gibberish syllable.
    syllable1 = input('Enter first gibberish syllable (add \'*\' for vowel substitute).\n')
    syllable2 = input('Enter second gibberish syllable (add \'*\' for vowel substitute).\n')
    
    #This is to call the add_gibberish function.
    translated_word = add_gibberish(syllable1, syllable2, word)
    print("Translated word: ", translated_word)
    

while True:
    #A while loop to prompt the user to play again or not. If they do want 
    #to play again, prompt this game again.
    print("\t\t- Gibberish Game -\n\n")
    word_to_translate = input("Enter a word to translate: ")
    word_translator(word_to_translate)
    
    play_again_prompt = input("Would you like to play again? [y/n or yes/no]\n")
    if play_again_prompt.lower() in ['n', 'no']:
        break

    

        
            
         
    