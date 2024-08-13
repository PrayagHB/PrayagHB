"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 03.4 -  Organisms 
Date: 02/05/2024

Description:
    This program predicts the size of the organism population based on ints multiplication rate.

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
    #This program predicts the size of the organism population based on ints multiplication rate.
    p=float(input("Starting population, in thousands: "))
    r=float(input("Average daily increase, in percent: "))
    d=float(input("Number of days to multiply: "))
    dc=0
    print(f"Day   Approx. Pop\n{dc:3}{p:14,.3f}\n",end='')
    while dc<d:
        p=p*(1+(r/100))
        dc+=1
        print(f"{dc:3}{p:14,.3f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
