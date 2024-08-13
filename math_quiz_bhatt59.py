"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 06.1 -  Math Quiz
Date: 02/22/2024

Description:
    This program generates two random variables and asks the user for their divison and displays if the user has entered correct answer or not.

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
import random as r

"""Write new functions below this line (starting with unit 4)."""
def random_factor(x):
    min=10**(x-1)
    max=(10**x)-1
    f=r.randint(min,max)
    return f

def main():
    #This program generates two random variables and asks the user for their divison and displays if the user has entered correct answer or not.
    f=random_factor(2)
    s=random_factor(1)
    n=f*s
    print(f' {n:3}\n\u00F7  {s}\n----')
    y=int(input("= "))
    if y==f:
        print("Great job, that's correct!")
    else:
        print(f'Sorry, the correct answer is {f}.')



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
