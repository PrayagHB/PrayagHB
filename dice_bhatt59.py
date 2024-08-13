"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 11.1 - Dice
Date: 04/02/2024

Description:
    This program defines a class called Dice which can be used to generate random numbers based on the number of sides of the dice and as many times as it is rolled.

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
class Dice:
        def __init__(self,sides):
            self.sides=sides
        def roll(self):
            k=r.randint(1,(self.sides))
            return k
        def n_rolls(self,n):
            l=[]
            while n!=0:
                l.append(self.roll())
                n-=1
            return l
        

def main():
    #This program defines a class called Dice which can be used to generate random numbers based on the number of sides of the dice and as many times as it is rolled.
    six_sided=Dice(6)
    ten_sided=Dice(10)
    twenty_sided=Dice(20)
    x=six_sided.n_rolls(10)
    y=ten_sided.n_rolls(10)
    z=twenty_sided.n_rolls(10)
    print("Rolling a 6 sided die 10 times: ",end="")
    for i in range(len(x)):
        if i == len(x) - 1:
            print(x[i], end="\n")
        else:
            print(x[i], end=", ")
    print("Rolling a 10 sided die 10 times: ",end="")
    for i in range(len(y)):
        if i == len(y) - 1:
            print(y[i], end="\n")
        else:
            print(y[i], end=", ")
    print("Rolling a 20 sided die 10 times: ",end="")
    for i in range(len(z)):
        if i == len(z) - 1:
            print(z[i], end="\n")
        else:
            print(z[i], end=", ")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
