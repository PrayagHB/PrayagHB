"""
Author: Your Name, login@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 02/19/2024

Description:
    This program draws a star based on the number of points entered by the user'

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    num_points=int(input('How many points you wnat on star?'))
    # Calculate the inner angle of the star points
    A = 360 / num_points
    # Calculate the concave angle between star points
    B = 2 * A

    # Set the initial angle for drawing
    initial_angle = 90-A

    # Draw the star
    begin_fill()
    right(initial_angle)
    for _ in range(num_points):
        forward(60)  # Length of each side
        left(180-A)
        forward(60) # Length of each side
        right(180-B)
    end_fill()
"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
