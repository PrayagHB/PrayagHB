"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 08.4 - Number Writer  
Date: 02/09/2024

Description:
    This program generates a file with random numbers in range 1119 to 1217  excluding all numbers whose digits sum to 13.

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
import os



"""Write new functions below this line (starting with unit 4)."""

        

def main():
    #This program generates a file with random numbers in range 1119 to 1217  excluding all numbers whose digits sum to 13.
    c=int(input("How many numbers would you like? "))
    i=0
    l=[]
    while i<c:
        k=r.randrange(1119,1218)
        k=str(k)
        sum=0
        for char in k:
            d=int(char)
            sum+=d
        if sum==13:
            continue
        else:
            l.append(k)
            i+=1
    s='\n'.join(l)
    with open('random_numbers.txt','w') as f:
        f.write(s)
    print(f"{c} numbers have been written to 'random_numbers.txt'.")
    #print(os.getcwd())     This command is to check the directory where the file is stored.
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
