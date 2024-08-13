"""
Author: Your Name, login@purdue.edu
Assignment: 05.4 - Turtle Writing
Date: 02/19/2024

Description:
    It writes a particular letter calling the functions

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


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")
    speed(0)


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


def draw_L():
    right(90)
    forward(130)
    left(90)
    forward(60)
    penup()
    forward(20)
    pendown()


def draw_o():
    penup()
    forward (30)
    pendown()
    circle(30)
    penup()
    forward(50)
    pendown()


def draw_p():
    penup()
    forward (30)
    pendown()
    circle(30)
    penup()
    backward(30)
    left(90)
    pendown()
    forward (60)
    backward(100)
    penup()
    forward(40)
    right(90)
    forward(60)
    forward(20)
    pendown()


def draw_S():
    forward (26)
    circle(32.25,180)
    circle(-32.25,180)
    forward (26)
    penup()
    right(90)
    forward(128.5)
    left(90)
    forward(20)
    pendown()

def draw_s():
    forward (11)
    circle(14.5,180)
    circle(-14.5,180)
    forward (11)
    penup()
    right(90)
    forward(60)
    left(90)
    forward(30)
    pendown()


def draw_T():
    penup()
    forward (30)
    left(90)
    pendown()
    forward(130)
    left(90)
    forward(30)
    backward(60)
    penup()
    left(90)
    forward(130)
    left(90)
    forward(10)
    pendown()


def draw_t():
    penup()
    forward (30)
    left(90)
    pendown()
    forward(130)
    backward(30)
    left(90)
    forward(30)
    backward(60)
    penup()
    left(90)
    forward(100)
    left(90)
    forward(10)
    pendown()


def main():
    #steps to move the cursor
    penup()
    backward(280)
    left(90)
    forward(50)
    right(90)
    pendown()
    #steps to write word "Steps"
    draw_S()
    draw_t()
    draw_e()
    draw_p()
    draw_s()
    #steps to move the cursor
    penup()
    forward(50)
    pendown()
    #steps to write word "To"
    draw_T()
    draw_o()
    penup()
    backward(550)
    right(90)
    forward(50)
    left(90)
    pendown()
    #steps to write word "Leaps"
    draw_L()
    draw_e()
    draw_a() 
    draw_p()
    draw_s()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
