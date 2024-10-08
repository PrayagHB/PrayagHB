"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 03.1 -  Cakes 
Date: 02/04/2024

Description:
    This program creates a visualization for a cake based on the number of layers the user enters.

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


def main():
    #This program creates a visualization for a cake based on the number of layers the user enters.
    x=int(input("Enter the number of layers: "))
    for i in range(x):
        y = " " * (x - i - 1)
        z = ""
        for j in range(2 * i + 1):
            z += "*"
        print(y + "[" + z + "]")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
