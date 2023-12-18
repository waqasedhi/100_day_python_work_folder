
import random
#from replit import clear
import os
#from art import logo

user_win = 0  
computer_win = 0

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    global user_win, computer_win
    if user_score > 21 and computer_score > 21:
        if user_score == computer_score:
            return "Draw 🙃"
        elif user_score < computer_score:
            user_win += 1 
            return "You win 😃"
        else:
            computer_win+=1
            return "You lose 😤"

    else:
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            computer_win+=1
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            user_win += 1 
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            computer_win+=1
            return "You went over. You lose 😭"
        elif computer_score > 21:
            user_win += 1 
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            user_win += 1 
            return "You win 😃"
        else:
            computer_win+=1
            return "You lose 😤"


def play_game():

    #print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False
    


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    compares=compare(user_score, computer_score)
    print(compares)
    
    is_end_process=False
    while not is_end_process:
        end_ask=input("Do you want to play a game of Number Guessing? for YES Type 'y' or any key to EXIT: ") == "y"
        if end_ask=="y":
            #clear()
            os.system('cls' if os.name == 'nt' else 'clear')
            play_game()
        else:
            is_end_process=True
            print("Take Care, Good Bye.")
    # while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    #     #clear()
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     print(f"user wins numbers {user_win}, computer wins numbers {computer_win}.")
    #     play_game()
    print(f"user wins numbers {user_win}, computer wins numbers {computer_win}.\n")
    
        
play_game()