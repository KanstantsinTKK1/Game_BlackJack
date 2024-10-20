from random import choice

from art import logo
import random

cards_name = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
status = bool
computer_status = bool
player_cards = []
computer_cards = []
player_score = int
computer_score = int

def start_game(gamer_cards, computer_stack):
    choice = input("Do you want to play a game of 'BlackJack'? Type 'y' on 'n': \n").lower()
    if choice == 'y':
        print("\n" * 20)
        print(logo)
        conditions = True
        gamer_cards.clear()
        computer_stack.clear()
    else:
        conditions = False
    return conditions


def add_cards(my_list):
    index = random.choice(range(len(cards)))
    my_list.append({cards_name[index]:cards[index]})


def sum_score(my_list):
    sum_cards = 0
    for card in range(len(my_list)):
        for value in my_list[card]:
            sum_cards += my_list[card][value]
    if sum_cards > 21:
        for pair in range(len(my_list)):
            for key in my_list[pair]:
                if key == 'A' and my_list[pair][key] == 11 :
                    sum_cards -= 10
                    my_list[pair][key] = 1
    return sum_cards


def print_cards():
    print (f"Your cards {player_cards}, current score: {player_score}")
    print (f"Computer's first card: {computer_cards}")
    y_or_n = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
    return y_or_n

status = start_game(player_cards, computer_cards)

while status:
    add_cards(player_cards), add_cards(player_cards)
    add_cards(computer_cards)
    player_score = sum_score(player_cards)
    computer_score = sum_score(computer_cards)
    computer_status = True
    if player_score == 21:
        continue_choice = 'n'
    else:
        continue_choice = print_cards()
    while continue_choice == 'y':
        add_cards(player_cards)
        player_score = sum_score(player_cards)
        if player_score > 21:
            continue_choice = 'n'
            add_cards(computer_cards)
            computer_score = sum_score(computer_cards)
            print(f"Your final hand {player_cards}, final score: {player_score}")
            print(f"Computer's final card: {computer_cards}, final score: {computer_score}")
            print("You went over. You lose :(\n")
            computer_status = False
        elif player_score == 21:
            continue_choice = 'n'
            computer_status = True
        else:
            continue_choice = print_cards()
            computer_status = True
    while computer_status:
        if computer_score < 17:
            add_cards(computer_cards)
            computer_score = sum_score(computer_cards)
        else:
            print(f"Your final hand {player_cards}, final score: {player_score}")
            print(f"Computer's final card: {computer_cards}, final score: {computer_score}")
            computer_status = False
    if computer_score > player_score and computer_score < 22:
        print("You lose :( \n")
    elif (player_score > computer_score and player_score < 22) or computer_score > 21:
        print("You win 😊\n")
    elif player_score == computer_score and player_score < 22:
        print("Draw!\n")
    status = start_game(player_cards, computer_cards)