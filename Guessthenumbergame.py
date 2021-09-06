#Guess The Number Game Chapter 4
import random
import time

def intro():
    global player
    player=input("Hello, what is your name?\n")
    #debugging line below
    global number
    number = random.randint(1,20)
intro()


def questionmath(userguess,guess):
    #I couldn't find the right word for this without making the name super long
    # This line below checks if the guess is greater than 20 or less than 1, than it checks if the userguess is greater or less than the number
    # Lastly it checks to see if the user guess is correct
    if(userguess > 20 or userguess < 1):
        print("Number isn't within 1 to 20!")
    elif(userguess > guess):
        print("Number is greater than my number.")
    elif(userguess < guess):
        print("Number is less than my number.")
    else:
        return userguess


for guesses in range(6,0,-1):
    time.sleep(1)
    playerguess = int(input("Hello, " + player + " I'm thinking of number between 1 to 20. \n Take a guess.\n You have " + str(guesses) + " left.\n"))
    
    questionmath(playerguess,number)
    if(playerguess == number):
            print("Congrats on beating me!!" + "\n Thanks for playing. \n Created by Marcello Alaniz @September 6th, 2021")
            time.sleep(0.5)
            exit()

#Ran out of guesses
print("Sorry " + str(player) + " but you have run out of guesses the answer was "+ str(number) + ".\n Thanks for playing. \n Created by Marcello Alaniz @September 6th, 2021")