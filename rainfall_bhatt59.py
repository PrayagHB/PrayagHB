"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 03.3 -  Rainfall 
Date: 02/05/2024

Description:
    This program gives a total and average rainfall for all the years entered by the users.

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
    #This program gives a total and average rainfall for all the years entered by the users.
    x=float(input("Enter the number of years: "))
    t,count,y=0,0,0
    list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    if x <=0:
        print('Invalid input; years must be greater than 0.')
    else:
        while y<x:
            print(f'  For year No. {y+1}')
            l,i=0,0
            while i<12:
                z=float(input("    Enter the rainfall for "+ list[l]+'.: '))
                if z>=0:
                    l+=1
                    t=t+z
                    count+=1
                    i+=1
                else:
                    print('    Invalid input; rainfall cannot be negative.')
                    continue
            y+=1
    if x > 0:
        avg=(t/count)
        print(f'There are {count} months.')
        print(f"The total rainfall was {t:,.2f} inches.")
        print(f"The monthly average rainfall was {avg:,.2f} inches.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
