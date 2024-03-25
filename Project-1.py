# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:06:19 2024

@author: jyoti
"""

import random

def get_user_choice():
    while True:
        user_choice = input('Choose snake, water or gun: ').lower()
        if user_choice in ['snake', 'water', 'gun']:
            return user_choice
        else:
            print('Invalid input! Choose once again.')

def get_comp_choice():
    return random.choice(['snake', 'water', 'gun']).lower()

def define_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie"
    elif (user_choice == 'snake' and comp_choice == 'Water') or \
         (user_choice == 'water' and comp_choice == 'gun') or \
         (user_choice == 'gun' and comp_choice == 'Snake'):
        return 'You win'
    else:
        return 'Computer wins'
        
def main():
    print('Welcome to snake, water, gun game!')
    while True:
        user_choice = get_user_choice() 
        comp_choice = get_comp_choice()
        print('You chose:', user_choice)
        print('Computer chose:', comp_choice)
        print(define_winner(user_choice, comp_choice))
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            break
        
if __name__ == "__main__":
    main()
