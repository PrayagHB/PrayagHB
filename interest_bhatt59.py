"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 01.2 - Interest
Date: 01/17/2024

Description:
    This program calculates the rate of compound interest based on the principal amount, interest and number of years.

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
    #This program calculates the rate of compound interest based on the principal amount, interest and number of years.
    print("Enter the following parameters.")
    p=float(input("  The initial deposit? "))
    r=float(input("  The annual interest rate in percent? "))
    t=float(input("  The number of years the account earn interest? "))
    n=float(input("  The number of times interest is compounded each year: "))
    fv=p*((1+(r/(n*100)))**(n*t))
    print(f"The balance of this account will be ${fv:,.2f} after {t:.1f} years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
