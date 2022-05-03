import os
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_draw(player_cards,is_it_dealer):
    if is_it_dealer == False:
        player_cards.append(random.choice(cards))
        if len(player_cards)<2:
            card_draw(player_cards,0)
    elif is_it_dealer == True:

        if len(player_cards) < 2 and 0 in cards:
            player_cards.append(random.choice(cards))
            card_draw(player_cards,1)
        elif sum(player_cards) < 17 and 0 in cards:
            player_cards.append(random.choice(cards))
    return player_cards

def is_it_ace(cards):
    counter = 0
    if 11 in cards:
        counter = cards.index(11)
    return counter


def calculate_sum(your_cards, dealer_cards):
    if sum(your_cards) > 21:
        print("You losse :[")
    elif sum(your_cards) > sum(dealer_cards):
        print("Your win :]")
    elif sum(your_cards) == sum(dealer_cards):
        print("It's a Draw")
    else:
        print("You losse :[")

def another_card(your_cards):
    mane_flag = False
    while mane_flag == False:
        another_card = input("Type 'y' to get another card type 'n' to pass: ").lower()
        if another_card == 'y':
            your_cards = card_draw(player_cards=your_cards, is_it_dealer=False)
            print(f"Your cards {your_cards} current score: {sum(your_cards)}")
        elif another_card == 'n':
            mane_flag = True
        else:
            print("Your input is Invalid plis choose correctley")
    return your_cards


def black_jack ():
    ace = 0
    clear = lambda: os.system('cls')
    clear()
    your_cards = []
    dealer_cards = []
    print(logo)
    your_cards = card_draw(player_cards=your_cards, is_it_dealer=False)
    dealer_cards = card_draw(player_cards=dealer_cards, is_it_dealer=False)
    print(f"Your cards {your_cards} current score: {sum(your_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")
    your_cards=another_card(your_cards)

    print(f'Your final hand: {your_cards}, final score {sum(your_cards)}')
    dealer_cards = card_draw(player_cards=dealer_cards, is_it_dealer=True)
    print(f"Computer's final hand: {dealer_cards}, final score {sum(dealer_cards)}")
    ace = is_it_ace(your_cards)
    if not ace == 0:
        choose = input(f"Your cards  contain ace do you wanna swith it's value to 1? Type 'y' or 'n': ").lower()
        if choose =='y':
            your_cards[ace]=1
            print(f'Your hand after changing ace value: {your_cards}, final score {sum(your_cards)}')
    calculate_sum(your_cards=your_cards, dealer_cards=dealer_cards)

    another_consent = input("Do you wanna play i BlackJack? type y or n: ").lower()
    if another_consent == 'y':
        black_jack()





consent = input("Do you wanna play i BlackJack? type y or n: ").lower()
if consent == 'y':
    black_jack()








