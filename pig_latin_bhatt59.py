"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 08.1 -  Pig Latin 
Date: 02/09/2024

Description:
    This program captures the input from user in pig latin and then translates it into a normal sentence.

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
def pig(a:str):
    l=a.split()
    c=0
    j=[]
    while c< len(l):
        p=l[c]
        p = p[-3] + p[:-3]
        j.append(p)
        c+=1
    f=' '.join(j)
    f=f.capitalize()
    return f
        

def main():
    #This program captures the input from user in pig latin and then translates it into a normal sentence.
    a=str(input('Enter a string in Pig Latin: '))
    k=pig(a)
    print(f'Translation: {k}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
