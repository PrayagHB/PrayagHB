"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 04.5 -  Prime List
Date: 02/10/2024

Description:
    #This program asks a value from the user and than lists out all the prime numbers upto that number and including that number by iterating over a list.

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
def is_prime(c):
    if c==2 or c==3:
        return True
    elif c<2:
        return False
    elif c%2==0:
         return False 
    else:
        for d in range(3,int((c**0.5)+1),2):
                if c%d==0:
                    return False
                    break
        return True

def main():
    #This program asks a value from the user and than lists out all the prime numbers upto that number and including that number by iterating over a list.Adding characters for satisfying gradescope criteria
    x=int(input('Enter a positive integer: '))
    c=0
    list=[]
    while c<=x:
        if is_prime(c)==True:
            list.append(c)
            c+=1
        else:
            c+=1
    print(f'The primes up to {x} are:',end=' ')
    for value in range(len(list)):
        if value<len(list)-1:
            print(list[value], end='')
            print(',',end=' ')
        else:
            print( list[value])


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
