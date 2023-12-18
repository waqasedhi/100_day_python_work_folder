#form replit import clear 
import os
import random

guessingNumber=random.randint(1,100)
attempts = 0

def guess_check(ask_guess):
    global attempts
    if ask_guess == guessingNumber:
        attempts=0
        print(f"You got it! the answer was {guessingNumber}")
    elif ask_guess > guessingNumber:
        attempts-=1
        print("Too high.\nGuess again.")
    elif ask_guess < guessingNumber:
        attempts-=1
        print("Too low.\nGuess again.")
    elif ask_guess>100 or ask_guess<1:
        attempts-=1
        print("provided number is out of range.\nGuess again.")

def play_game():
    global attempts
    print ("Welcome to the Number Guessing Game! \nI'm thniking of a number between 1 to 100. ")
    ask = input ("Chose a difficulty. type 'easy' or 'hard': ").lower()
    #print(guessingNumber)
    if ask == "easy":
        attempts=10
        print(f"you have {attempts} attempts remainnig to guess the number. ")
        while attempts>0:
            ask_guess= int(input("Make a guess: "))
            guess_check(ask_guess)
            print(f"Your remaining attempts are {attempts}\n")
       
    elif ask== "hard":
        attempts=5
        print(f"you have {attempts} attempts remainnig to guess the number. ")
        while attempts>0:
            ask_guess= int(input("Make a guess: "))
            guess_check(ask_guess)
            print(f"Your remaining attempts are {attempts}\n")
            
    else:
        print("You given a worng input.")
    
    is_end_process=False
    
    while not is_end_process:
        #print(is_end_process)
        end_ask=input("Do you want to play a game of Number Guessing? for YES Type 'y' or any key to EXIT: ").lower()
        if end_ask=="y":
            #clear()
            os.system('cls' if os.name == 'nt' else 'clear')
            play_game()
        else:
            is_end_process=True
            #print(is_end_process)
            print("Take Care, Good Bye.")

play_game()