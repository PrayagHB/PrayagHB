"""
Author: Your Name, login@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 02/24/2024

Description:
    This program will import the vowels program that contains the functions that will be used by the random function to draw vowels randomly.

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels as v
import random as r


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    #This program will import the vowels program that contains the functions that will be used by the random function to draw vowels randomly.
    l=['a','e','i','o','u']
    r.shuffle(l)
    for i in range(len(l)):
        if l[i]=='a':
            v.draw_a()
        elif l[i]=='e':
            v.draw_e()
        elif l[i]=='i':
            v.draw_i()
        elif l[i]=='o':
            v.draw_o()
        elif l[i]=='u':
            v.draw_u()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
