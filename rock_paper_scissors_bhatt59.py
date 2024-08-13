"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 06.2 -  Rock Paper Scissors
Date: 02/22/2024

Description:
    This program determines the winner for the game of rock paper scissors based on the input entered by user.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random as r

"""Write new functions below this line (starting with unit 4)."""
def get_computer_choice():
    l=['rock','paper','scissors']
    c=r.choice(l)
    return c

def get_player_choice():
    l=['rock','paper','scissors']
    while True:
        c=input('Choose rock, paper, or scissors: ')
        if c in l:
            return c
        else:
            print('You made an invalid choice. Please try again.')

def get_winner(f,s):
        l=['rock','paper','scissors']
        if (l[1]==f and l[0]==s) or (l[0]==f and l[2]==s) or (l[2]==f and l[1]==s):
             return "computer"
        elif (l[1]==s and l[0]==f) or (l[0]==s and l[2]==f) or (l[2]==s and l[1]==f):
             return "player"
        else:
             return 'tie'

def main():
    # This program determines the winner for the game of rock paper scissors based on the input entered by user and provides output based on the winner decided from the player or the computer.
    while True:
        f=get_computer_choice()
        s=get_player_choice()
        k=get_winner(f,s)
        print(f'  The computer chose {f}, and you chose {s}.')
        if k=='player':
            print(f'  {s} beats {f}\n  You won the game!\nThanks for playing.')
        elif k=='computer':
            print(f'  {f} beats {s}\n  You lost.  Better luck next time.\nThanks for playing.')
        else:
            print("  It's a tie. Starting over.\n")
        if k=='tie':
            continue
        else:
            break


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
