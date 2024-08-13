"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 01.1 - Road trip
Date: 01/17/2024

Description:
    This program provides the estimated fuel cost for a road trip.

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
    # a program to indicate use of input and ouput functions to estimate the cost of fuel based on the given formula
    print("Road trip fuel cost estimator:")
    d=int(input("  How far away is your destination (miles)? "))
    p=float(input("  What is the average price of gas (dollars per gallon)? "))
    m=float(input("  What is the fuel efficiency of your vehicle (mpg)? "))
    c=int((2*d)*p/m)
    print(f"\nThe fuel cost for this trip is approximately ${c}.")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
