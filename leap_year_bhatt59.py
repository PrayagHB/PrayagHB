"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 02.1 - Leap year
Date: 01/25/2024

Description:
    This program allows the user to determine if the year entered is a leap year or not.

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
    #This program allows the user to determine if the year entered is a leap year or not.
    x=int(input("Enter a year: "))
    if (x%4==0 and x%100!= 0) or (x%400==0):
        print(f"The year {x} is a leap year.\nFebruary of {x} has 29 days.")
    else:
        print(f"The year {x} is not a leap year.\nFebruary of {x} has 28 days.")
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
