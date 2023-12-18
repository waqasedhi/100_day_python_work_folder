from game_data import data
import random
import os
from art import *
from methods import * 

user_win = 0   
compare=[] 

def play():
    global user_win 
    global compare
    
    result="win"
    
    while result == 'win' or result=='draw':
        print(logo)
        print(f"user wins numbers {user_win}")
        if compare==[]:
            compare=compare1()
        else:
            compare.pop(0)
            compare.append(compare2(compare))
        a=data[compare[0]]
        b=data[compare[1]]
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against A: {b['name']}, a {b['description']}, from {b['country']}.")
        answer=input("who has more follower? type 'A' or'B': ").lower()
        result= chk_flw ( a,b,answer)
        if result=='win':
            user_win +=1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ( f"Sorry, that's wrong. Final score: {user_win}")
play()