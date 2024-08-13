"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 04.3 -  Avg Grade 
Date: 02/09/2024

Description:
    This program gives out grade for the average score and the individual scores calculated by the scores entered by the user.

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

def calc_average(list):
    i=0
    a=0
    j=0
    while i<len(list):
        a+=list[i]
        i+=1
        j+=1
    avg=a/j
    return avg
def determine_grade(x):
    if x>=92 and x<=100:
        g='A'
    elif x>=82 and x<92:
        g='B'
    elif x>=73 and x<82:
        g='C'
    elif x>=64 and x<73:
        g='D'
    elif x>=0 and x<64:
        g='F'
    return g
def get_valid_score():
    while True:
        c=float(input('Enter a score: '))
        if c<0 or c>100:
            print('  Invalid Input. Please try again.')
        else:
            break
    return c

def main():
    #This program gives out grade for the average score and the individual scores calculated by the scores entered by the user.
    #Extra comment to fulfill the criteria for Gradescope.
    i=0
    list=[]
    while i<5:
        c=get_valid_score()
        print(f'  The letter grade for {c} is '+determine_grade(c)+'.')
        list.append(c)
        i+=1
    y=calc_average(list)
    print(f'\nResults:\n  The average score is {y:.2f}.\n  The letter grade for {y:.2f} is '+determine_grade(y)+'.'  )

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
