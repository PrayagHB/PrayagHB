"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 02.5 -  fluid Mechanics
Date: 01/27/2024

Description:
    This program calculates the Reynolds Number of the fluid by taking Velocity,Diameter and Temperature as input.

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
    #This program calculates the Reynolds Number of the fluid by taking Velocity,Diameter and Temperature as input.
    t=float(input("Enter the temperature in °C as 5, 20, or 50: "))
    v=float(input("Enter the velocity of water in the pipe (m/s): "))
    d=float(input("Enter the pipe's diameter (m): "))
    if t==5:
        k=1.52e-06
    elif t==20:
        k=1e-06
    else:
        k=5.54e-07
    r=(v*d)/k
    print(f"At {t:.1f}°C, the Reynolds number for flow at {v} m/s in a {d} m diameter pipe is {r:.2e}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
