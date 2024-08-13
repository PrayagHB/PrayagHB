"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 02.2 - Software Sales
Date: 01/14/2024

Description:
    This program calculates the discount given on a software purchase based on the number of quantity.

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
    #This program calculates the discount given on a software purchase based on the number of quantity.
    x=int(input("How many packages will be purchased: "))
    if x>=0 and x<=3:
        a=880*x
        print(f"  No discount applied.\n  The total price to purchase {x} packages is ${a:,.2f}.")
    elif x>=4 and x<=39:
        a=880*0.9*x
        print(f"  10% discount applied.\n  The total price to purchase {x} packages is ${a:,.2f}.")
    elif x>=40 and x<=199:
        a=880*0.85*x
        print(f"  15% discount applied.\n  The total price to purchase {x} packages is ${a:,.2f}.")
    elif x>=200 and x<=999:
        a=880*0.7*x
        print(f"  30% discount applied.\n  The total price to purchase {x} packages is ${a:,.2f}.")
    elif x>=1000:
        a=880*0.58*x
        print(f"  42% discount applied.\n  The total price to purchase {x} packages is ${a:,.2f}.")
    else:
        print("  Invalid Input!")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
