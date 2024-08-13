"""
Author: Your Name, login@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 02/24/2024

Description:
    This program generates functions that will be used to draw vowels in the random_vowels program by importing this program.

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
from turtle import *


"""Write new functions below this line (starting with unit 4)."""


def draw_a():
    penup()
    forward (30)
    pendown()
    circle(30)
    penup()
    forward(30)
    left(90)
    pendown()
    forward (60)
    backward(60)
    penup()
    right(90)
    forward(20)
    pendown()

def draw_e():
    penup()
    forward (50)
    backward(7)
    left(90)
    forward(9)
    left(135)
    pendown()
    circle(-30,315)
    right(90)
    forward(50)
    penup()
    backward(50)
    left(90)
    forward(30)
    left(90)
    forward(20)
    pendown()

def draw_i():
    pendown()
    left(90)
    forward(60)
    penup()
    forward(20)
    pendown()
    forward(1)
    penup()
    backward(81)
    right(90)
    forward(30)
    pendown()

def draw_o():
    penup()
    forward (30)
    pendown()
    circle(30)
    penup()
    forward(50)
    pendown()



def draw_u():
    penup()
    forward (50)
    backward(7)
    left(90)
    forward(9)
    left(135)
    pendown()
    circle(-30,140)
    left(5)
    forward(30)
    penup()
    backward(30)
    right(180)
    circle(30,140)
    left(40)
    pendown()
    forward(50)
    backward(70)
    penup()
    forward(5)
    right(90)
    forward(20)
    pendown()

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
    #This program generates functions that will be used to draw vowels in the random_vowels program by importing this program.
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    pass


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
