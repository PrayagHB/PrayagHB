"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 02.3 -  Roulette Colors 
Date: 01/26/2024

Description:
    This program provides the color of the pocket based on the selection of the pocket number.

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
    #This program provides the color of the pocket based on the selection of the pocket number.
    x=int(input("Please choose a pocket number: "))
    if x==0:
        print(f"  Pocket number {x} is green.")
    elif x>=1 and x<=10:
        if x%2==0:
            print(f"  Pocket number {x} is black.")
        else:
            print(f"  Pocket number {x} is red.")
    elif x>=11 and x<=18:
        if x%2==0:
            print(f"  Pocket number {x} is red.")
        else:
            print(f"  Pocket number {x} is black.")
    elif x>=19 and x<=28:
        if x%2==0:
            print(f"  Pocket number {x} is black.")
        else:
            print(f"  Pocket number {x} is red.")
    elif x>=29 and x<=36:
        if x%2==0:
            print(f"  Pocket number {x} is red.")
        else:
            print(f"  Pocket number {x} is black.")
    else:
        print("  Invalid Input!")
        
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
