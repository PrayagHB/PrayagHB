"""
Author: Your Name, login@purdue.edu
Assignment: 07.2 - Spiral
Date: 03/02/2024

Description:
    This program draws a loop of squares to form a spiral.

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
def interpolate_point(a,b,c):
    xa,ya=a
    xb,yb=b
    xnew=xa+(c*(xb-xa))
    ynew=ya+(c*(yb-ya))
    return xnew,ynew


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(700, 500)
    width(3)
    speed(0)


def main():
    #This program draws a loop of squares to form a spiral.
    penup()
    goto(-100,-100)
    pendown()
    for _ in range(4):
        forward(200)
        left(90)
    penup()
    goto(100,100)
    pendown()
    right(90)
    a=(100,-100)
    b=(-100,-100)
    c=(-100,100)
    d=(100,100)
    cc=0
    while cc<40:
        x=interpolate_point(a,b,0.1)
        goto(x)
        a=x
        right(90)
        y=interpolate_point(b,c,0.1)
        goto(y)
        b=y
        z=interpolate_point(c,d,0.1)
        goto(z)
        c=z
        e=interpolate_point(d,a,0.1)
        goto(e)
        d=e
        cc+=1
        

    


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
