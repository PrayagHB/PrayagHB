"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 04.2 -  Lucky Sum 
Date: 02/08/2024

Description:
    This program adds all the integers divisble by 7 between the range of numbers that are entered by the user.

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
def lucky_sum(i,f):
    x=0
    if i>=f:
        while f<=i:
            if f%7==0:
                x+=f
            f+=1
    else:
        while i<=f:
            if i%7==0:
                x+=i
            i+=1
    return x

def main():
    #This program adds all the integers divisble by 7 between the range of numbers that are entered by the user.
    i=int(input("Enter the first integer: "))
    f=int(input("Enter the second integer: "))
    x=lucky_sum(i,f)
    print(f'The sum of the lucky numbers is {x:,}.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
