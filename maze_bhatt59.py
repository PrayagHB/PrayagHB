"""
Author: Your Name, login@purdue.edu
Assignment: 05.1 - Maze
Date: 02/14/2024

Description:
    This program depeicts the path of turtle to go out of the maze.

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
    setup(564, 564)
    bgpic(r"C:\Users\h\Desktop\EBEC Entry-Level Programming in Python\python_work\unit 05\maze.png") # Here r is added to escape the '\' so we can use the file path to access the image file
    shape("turtle")
    color("green")
    width(5)


def main():
    left(90)
    forward(12)
    left(90)
    forward(85)
    right(90)
    forward(72)
    right(90)
    forward(97)
    left(90)
    forward(25)
    right(90)
    forward(47)
    left(90)
    forward(23)
    right(90)
    forward(144)
    right(90)
    forward(47)
    right(90)
    forward(23)
    left(90)
    forward(23)
    left(90)
    forward(47)
    right(90)
    forward(63)
    left(90)
    forward(25)

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
