"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 01/17/2024

Description:
    This program suggests the user, the amount of ingredients they require for making a specific amount of cookies.

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
    #This program suggests the user, the amount of ingredients they require for making a specific amount of cookies.
    x=int(input("How many cookies do you want to make? "))
    b=(x*1.25)/48
    s=(x*1.5)/48
    f=(x*2.5)/48
    print(f"To make {x:,d} cookies, you will need:\n{b:10,.2f} cups of butter\n{s:10,.2f} cups of sugar\n{f:10,.2f} cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
