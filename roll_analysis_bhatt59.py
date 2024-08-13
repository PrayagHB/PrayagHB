"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 07.3 -  Roll Analysis 
Date: 03/03/2024

Description:
    This program gives the frequency of the outcome of a particular number when two dice are rolled.

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
def roll_d6():
    x=r.randrange(1,7)
    return x

def get_2d6_rolls(c):
    l=[]
    k=0
    while k<c:
        s=roll_d6()+roll_d6()
        l.append(s)
        k+=1
    return l

def main():
    #This program gives the frequency of the outcome of a particular number when two dice are rolled.
    o=get_2d6_rolls(9)
    o.sort()
    print('Roll  Frequency')
    i=0
    while i<(len(o)):
        if o.count(o[i])==1:
            p=(o.count(o[i])/len(o))*100
            print(f'{o[i]:3}   {p:6.2f}%')
            i+=1
        elif o.count(o[i])>1:
            p=(o.count(o[i])/len(o))*100
            print(f'{o[i]:3}   {p:6.2f}%')
            i+=(o.count(o[i]))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
