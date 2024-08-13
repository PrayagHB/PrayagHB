"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 04.1 -  falling 
Date: 02/08/2024

Description:
    This program calculates the falling speed of an object on venus.

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

"""Write new functions below this line (starting with unit 4)."""
def falling_dist (t):
    g=8.87
    d=0.5*g*t**2
    return d

def main():
    #This program calculates the falling speed of an object on venus.
    print('Time (s)  Distance (m)')
    print('-'*22)
    for t in range (5,51,5):
        x=falling_dist(t)
        print(f'{t:8,d}{x:14.1f}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
