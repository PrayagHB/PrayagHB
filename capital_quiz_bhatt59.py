"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 09.1 - Capital Quiz 
Date: 03/21/2024

Description:
    This program provides a quiz of US states and their capitals wherein user has to name the capital based on the given state.

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
def get_state_data():
    d = {}
    with open("state_capitals.txt") as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                value, key = parts
                key = key.strip()
                d[key] = value
    return d

        

def main():
    #This program provides a quiz of US states and their capitals wherein user has to name the capital based on the given state.
    d=get_state_data()
    k=list(d.keys())
    v=list(d.values())
    total=0
    correct=0
    while k:
        r.shuffle(k)
        state=k.pop()
        city=str(d[state])
        i=(input(f'What is the capital of {state} (enter 0 to quit)? '))
        if i!='0':
            i=str(i)
            if i.lower()==city.lower():
                total+=1
                correct+=1
                print('  That is correct!')
            else:
                total+=1
                print(f'  That is incorrect.\n  The capital of {state} is {city}.')
                k.append(state)
        else:
            break
    if total!=0:
        c=(correct/total)*100
        print(f'You answered {c:.1f}% of the questions correctly.')
    else:
        print("You didn't answer any questions.")
    

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
