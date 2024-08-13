"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 07.1 -  Data Parsing 
Date: 02/29/2024

Description:
    This program determines whether the number entered by the user is a prime number or not.

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
from data import data


"""Write new functions below this line (starting with unit 4)."""


def main():
    #
    print('          :  Price\n  Decade  : in 2021\n          : Dollars\n-------------------')
    i=0
    j=0
    p=i+36
    k=3
    sum=0
    while j < len(data):
        c=0
        while c<10:
            if k>len(data):
                #k=(len(data)-1)
                #sum= sum+data[k]
                break
            else:
                sum= sum+data[k]
                k+=4
                c+=1
        j+=40
        avg=(sum/c)
        if p>len(data):
            print(f'{data[i]}-'+f'2029 :  ${avg:.3f}')
        else:
            print(f'{data[i]}-{data[p]} :  ${avg:.3f}')
        sum=0
        i+=40
        p=i+36
    #print('2020-2029 :  $3.381')



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
