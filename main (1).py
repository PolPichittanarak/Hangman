import random # allows random function
import turtle # allows turtle function
screen = turtle.getscreen()#displays a screen
hangman = turtle.Turtle()#gets turtle
hangman.shapesize(0.1, 0.1,0.1) # sets the size
hangman.pensize(3) # sets the pen size
hangman.penup() 
hangman.goto(0,-50) # turtle goes to the starting point

print("Welcome to Hangman!!!") # greeting text
custom = False #valid input check
while not custom:
	custominput = input("would you like to customize your hangman?\n").lower().strip() # asks for the user input
	if custominput == "yes":# if the answer is yes
		validcolor = False #valid input check
		while not validcolor:
			avaliablec = ["black", "red", "blue", "green", "yellow" ,"brown", "purple", "orange"]#list of available colors
			print("the available choices are \n-{}".format("\n-".join(avaliablec))) # displays the list to the user
			colorinput = input("what color would you like your hangman to be? (please enter a color in the available choices)\n").lower().strip()#asks the user for an input and stores it as colorinput
	
			if colorinput in avaliablec:# checks if the color the user entered avaliable
				print("The pen color is set to {}".format(colorinput))#informs the user that the pen color has been changed
				validcolor = True 
				hangman.pencolor(colorinput)# sets the pen color to the color that the user chose earlier
			else: # checks if the user input is not in the list
				print("Unavailable color\nPlease enter a color from the available choices.\n") # informs the user that the color the entered is unavailable
		custom = True# the user input is valid
	elif custominput == "no":# if the answer is no
		custom = True# the user input is valid
		print("Your hangman is set to default.") # informs the user that the pen color is set to default
		hangman.pencolor("black") # sets the pen color to black
		validcolor = True 
	
	else: # if the user input is invalid (not yes or no)
		print("please enter only yes or no\n") #asks the user to enter only yes or no
valid = False# valid input check
while not valid: 
	randomorpick = input("would you like to pick your own word?\n").lower().strip() # asks the user of they would like to pick the word and stores it as randomorpick
	if randomorpick == "yes":# if the answer is yes
		valid = True # valid input
		wordvalid = False # valid input check
		while not wordvalid:
			wordinput = input("what would you like your word to be?\n").lower().strip() # asks the user to enter the word and stores it as wordinput
			if len(wordinput) <= 1: # check if the word is too short
				print("The minimum word length is 1\n") #tells the user that the minimum word length is 1
			else: # if the word is not too short
				for letters in range(len(wordinput)): # checks if all the characters are alphabetical characters
					if wordinput[letters].isalpha():# if every characters is an alphabetical character
						wordvalid = True # word valid
					else:# if the word contains character(s) which is not alphabetical
						print("{} is invalid, please enter a word containing only alphabetical characters.\n".format(wordinput)) # informs the user that the word is invalid due to the fact that it's containing unalphabetical chatacter(s)
						wordvalid = False #word invalid
						break
		print("okay your word is set to {}".format(wordinput))# informs the user that the word has been set
		chosen_word = wordinput # set the word to the word that the user entered earlier
		word_length = len(chosen_word) # word length
		spaces = "_ " * word_length # spaces according to the word length 
		word = list(chosen_word) # list of all the letters in the word
		word_spaces = list(spaces)# list of all the spaces in the spaces variable
				
			
	elif randomorpick == "no": # if the user does't want to pick their own word
		valid = True # valid input
		print("Okay! Your word will be picked at random.")
		word_list = ["game", "hangman", "random"] #words source
		chosen_word = random.choice(word_list) #ramdomized
		word_length = len(chosen_word) # word length
		spaces = "_ " * word_length # spaces according to the word length
		word = list(chosen_word) # list of all the letters in the word
		word_spaces = list(spaces) # list of all the spaces in the spaces variable
	
	else:  # if the user input is neither a yes or no (invalid)
		print("please enter only yes or no\n") # asks the user to enter only yes or no


letter_index = []# list for storing the letter index(indices)
lives = 9 #trial limit
letter_guessed = [] #letters that have been guessed
char_allowed = ["a", "b", "c", "d", "e", "f","g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # list of the characters allowed

def line1():
  hangman.pendown()
  hangman.left(180)
  hangman.forward(50)
  hangman.right(90)
  hangman.forward(150)

def line2():
  hangman.right(90)
  hangman.forward(75)

def line3():
  hangman.right(90)
  hangman.forward(20)

def line4():
  hangman.right(90)
  hangman.circle(10)

def line5():
  hangman.penup()
  hangman.left(90)
  hangman.forward(20)
  hangman.pendown()
  hangman.forward(50)

def line6():
  hangman.penup()
  hangman.left(180)
  hangman.forward(40)
  hangman.left(135)
  hangman.pendown()
  hangman.forward(20)
  hangman.left(180)
  hangman.forward(20)

def line7():
  hangman.right(90)
  hangman.forward(20)
  hangman.left(180)
  hangman.forward(20)
  hangman.left(135)
  hangman.forward(40)

def line8():
  hangman.right(45)
  hangman.forward(20)
  hangman.right(180)
  hangman.forward(20)
  hangman.right(90)

def line9():
  hangman.forward(20)


print("""Your word has {} letters.
You have {} lives.
Good Luck!\n""".format(word_length, lives))
print(spaces) # displays the spaces 
while "_" in word_spaces: #check if the player has already lost or won

	letter = input("Guess a letter: ").strip().lower() 
#letter input
	
		
	if len(letter) != 1: #if the input contains more than 1
		print("Please enter 1 letter at a time\n")
	else: # if the user input contain only a single letter
		if lives >= 0: # checks the user lives
			if letter in char_allowed: # check if the letter the user entered is valid
				if letter in letter_guessed: #if the letter has already been guessed
					print("This letter has been guessed. \nLetters guessed: {}\n".format(",".join(letter_guessed)))

				elif letter in word: #if the letter is correct
					print("correct \n{} is in the word\n".format(letter))
					for index in range(word_length): 
						letter1 = chosen_word[index]
						if letter1 == letter: #identifies the index(indices) of the correct letter
							letter_index.append(index) # adds the letter index(indices) to the list of the charater index(indices)
						for i in letter_index:
							letter_position = letter_index[0]*2# the letter index
							word_spaces.pop(letter_position) # removes the underscore (_) at the index of the correct letter that has been guessed
							word_spaces.insert(letter_position, letter)# replaces the space(s) with the correct letter
							letter_index.pop(0)# clear the list of the character index(indices)
					print("".join(word_spaces))
					letter_guessed.append(letter) # adds the letter guessed by the user to the list 

				elif letter not in word: #if the letter is incorrect
					print("incorrect, try again")
					lives -= 1 #lives deducted
					print("you have {} lives\n".format(lives)) #informs the user the number of remaining lives
					letter_guessed.append(letter) # adds the letter guessed by the user to the list 
					if lives == 8: # if the user has 8 lives remaining
						line1() # draws the first line of hangman
					elif lives == 7: # if the user has 7 lives remaining
						line2()# draws the second line of hangman
					elif lives == 6:# if the user has 6 lives remaining
						line3()#draws the third line of hangman
					elif lives == 5:# if the user has 5 lives remaining
						line4()# draws the fourth line of hangman
					elif lives == 4:# if the user has 4 lives remaining
						line5() # draws the fifth line of hangman
					elif lives == 3:# if the user has 3 lives remaining
						line6()# draws the sixth line of hangman
					elif lives == 2:# if the user hs 2 lives remaining
						line7() # draws the seventh line of hangman
					elif lives == 1: # if the user has 1 life remaining
						line8()# draws the eighth line of hangman
					elif lives == 0:# if the user has 0 life remaining
						line9() # draws the last line of hangman
						print("YOU LOSE! \nThe correct answer is {}".format(chosen_word)) # informs that the user has lost
						break
			else:
				print("please enter an alphabetical character\n")# asks the user to enter only an alphabetical characyer
    
if "_" not in word_spaces:  #checks if all the letters have been guessed
  print("\nYOU WIN! \nThe word is {}".format(chosen_word))# informs that the user has won the game
  
#a) is almost functional needs to add a game over when game is finished 
#b) no
#c) could add hangman being drawn every time they get a wrong awnser
#d) yes 

  
  

