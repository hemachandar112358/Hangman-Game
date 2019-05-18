'''
Created on 19-Feb-2019

@author: Hemachandar
'''
import random

valid_alphabets="abcdefghijklmnopqrstuvwxyz";

file=open('WordsList');
words=file.readlines();
word= random.choice(words);
word_random=word.strip();

file.close()

l = len(word_random)

choices=5;

guessed_Word=['_']*l;

previous_CorrectGuesses=[]; '''Saves correct guesses of player'''
previous_IncorrectGuesses=[]; '''Saves Incorrect guesses of player to inform it has already been used'''


print("Welcome to Hangman Game\n You have 5 guesses to choose the word correctly.");

while(choices>0):
    chosen_letter= input("\nEnter your letter: \n").lower();
    if chosen_letter in previous_IncorrectGuesses or chosen_letter in previous_CorrectGuesses:
        print("Already guessed this letter. Please guess another letter");
    else:
        if chosen_letter in valid_alphabets and len(chosen_letter)==1:
    
            if chosen_letter in word_random:
                previous_CorrectGuesses.append(chosen_letter)
                
            
                for i in range(0,l):
                    if chosen_letter in word_random[i]:
                        guessed_Word.pop(i)
                        guessed_Word.insert(i,chosen_letter)
                        
                print(*guessed_Word);                         
               
                word_guessed=''.join(guessed_Word);
                if word_guessed==word_random:
                    print("You Won!!!")
                    break
                else:
                    continue;
                
            else:
                print("Wrong Guess !!!")
                previous_IncorrectGuesses.append(chosen_letter)
                choices=choices-1;
                print('Number of Choices left: ',choices);
        else:
            print("Enter a single valid alphabet")
   
if(choices==0):
    print("Game over")
print("The word was: "+word_random)    


    

        
        
    
    



















