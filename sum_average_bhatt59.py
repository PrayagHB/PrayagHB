"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 03.2 -  Sum Average
Date: 02/04/2024

Description:
    This program gives a sum and average of all the numbers entered except the negative numbers.

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
    #This program gives a sum and average of all the numbers entered except the negative numbers.
    t=0
    c=0
    while True:
        x=float(input("Enter a non-negative number (negative to quit): "))
        if x>=0:
            t+=x
            c+=1
        else:
            break
    if c>0:
        avg=t/c
        print(f"  You entered {c} numbers.\n  Their sum is {t:,.3f} and their average is {avg:,.3f}.")
    else:
        avg =0
        print("  You didn't enter any numbers.")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
