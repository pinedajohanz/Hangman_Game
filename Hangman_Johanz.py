#while loop and for loop
#if-else statement

import time
from random import choice

print('''

▒█░▒█ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ █ 
▒█▀▀█ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▀ 
▒█░▒█ ▒█░▒█ ▒█░░▀█ ▒█▄▄█ ▒█░░▒█ ▒█░▒█ ▒█░░▀█ ▄

''')
print()

# guess the word
words = ["bootcamp", "software", "webdevelopment", "python", "discord", "microsoft", "coding", "philippines"]
letters_guessed = ""
random_word = choice(words) # to choose a random word within the array

# hangman figure to be insert after wrong guess
figure = [
    '''
			 ________      
			 |      |      
			 |             
			 |             
			 |             
			 |             
		''',
'''
			 ________      
			 |      |      
			 |      0      
			 |             
			 |             
			 |             
		''',
        '''
			 ________      
			 |      |      
			 |      0      
			 |     /       
			 |             
			 |             
		''',
		'''

			 ________      
			 |      |      
			 |      0      
			 |     /|      
			 |             
			 |           
		''',
		'''	

			 ________      
			 |      |      
			 |      0      
			 |     /|\      
			 |             
			 |            

		''',
		'''	

			 ________      
			 |      |      
			 |      0      
			 |     /|\      
			 |     /         
			 |            
		''',
        ''' 

			 ________      
			 |      |      
			 |      0      
			 |     /|\      
			 |     / \         
			 |          
''']

# The number of turns before the user loses
failure_count = 7

start_time = int(time.time()) # start of countdown timer

# Loop until the user has made too many failed attempts

while failure_count > 0: # while loop as long as failure count is greater than 0
    print(" Let's Play Hangman!") 
    guess = input(("Enter a letter here: ")) # the user will input the guess letter
    print()
    cur_time = int(time.time()) 
    time_left = 30 - (cur_time - start_time) # displays current time left (30 - current time - start time) equals to negative number equates to countdown to 0

    if (cur_time - start_time) >= 30:
        print(figure[-1])
        print("Time's up! Game over! Better luck next time. You have been hanged!") # if time left exceed equals to end of game
        break 
        
    print("Time Left:", time_left) # print time remaining in every input of the user
    
    if guess in random_word: 
        print(f"Nice Job! You got it!") # print this if user guess a correct letter
    else:
        failure_count -= 1
        print(f"Awch! You got it wrong. There are no {guess} in the random word. {failure_count} turn(s) left.") # print this if user guess an incorrect letter
        print(figure[6-failure_count]) # print this to show figure of hangman according to wrong guess count
        

    # Maintain a list of all letters guessed
    letters_guessed = letters_guessed + guess
    wrong_letter_count = 0 # wrong letter start

    for letter in random_word:
        if letter in letters_guessed:
            print(f"{letter}", end = "") # print the correct guessed letter
        else:
            print("_", end = "") # print the underscore if wrong guess 
            wrong_letter_count += 1

    #if there were no wrong letters, then the user won. Print below
    if wrong_letter_count == 0:
        print()
        print(f"Congratulations! You successfully guessed the random word: {random_word}.")
        print()
        break # stop the loop

else: 
    print()
    print("Sorry! You failed to guess the random word. You have been hanged! GAME OVER!") #print this if the user ran out of turns
    


#done


''''''''''''''''''''''


import time

for i in range(30, 0, -1):
    print(i)
    time.sleep(2)
print("Time's up! Game over! Better luck next time.")

'''''''''''''''''''''