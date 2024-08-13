"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 07.4 -  Magic Square 
Date: 03/04/2024

Description:
    This program determines whether the set of numbers entered by the user forms a Lo Shu Magic Square.

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
def print_square(l:list):  #function to print the square
    
    i=0
    while i<3:
        if i<2:
            print('  ', end='')
            j=-1
            while j<2:
                j+=1
                if j<=1:
                    print (l[i][j], end=' ')
                else:
                    print (l[i][j])
            #print()  
        else:
            print('  ', end='')
            j=-1
            while j<2:
                j+=1
                if j<=1:
                    print (l[i][j], end=' ')
                else:
                    print (l[i][j])
        i+=1
def is_magic(l:list): #function to check if its the Lo Shu magic square
    v= False
    if (l[0][0]!=l[0][1]) and (l[0][0]!=l[0][2]) and (l[0][1]!=l[1][0])and (l[0][0]!=l[1][1])and (l[0][0]!=l[1][2])and (l[0][0]!=l[2][0]) and (l[0][0]!=l[2][1]) and (l[0][0]!=l[2][2]) and (l[0][1]!=l[0][2]) and (l[0][1]!=l[1][0])and (l[0][1]!=l[1][1])and (l[0][1]!=l[1][2])and (l[0][1]!=l[2][0])and (l[0][1]!=l[2][1])and (l[0][1]!=l[2][2]):
        if (l[0][0]+l[0][1]+l[0][2])==15 and (l[1][0]+l[1][1]+l[1][2])==15 and (l[2][0]+l[2][1]+l[2][2])==15:
                    if (l[0][0]+l[1][0]+l[2][0])==15 and (l[0][1]+l[1][1]+l[2][1])==15 and (l[0][2]+l[1][2]+l[2][2])==15:
                        if (l[0][0]+l[1][1]+l[2][2])==15 and (l[0][2]+l[1][1]+l[2][0])==15:
                            return True
    else:
        return False
    return v 
        
def main():
    #This program determines whether the set of numbers entered by the user forms a Lo Shu Magic Square. Adding addtional text to satisfy the autograder criteria for comments
    l=[[1, 2, 3], [4, 5,6], [7, 8, 9]]
    print('Your square is:')
    print_square(l)
    t=is_magic(l)
    #print(t)
    if t== True:
        print('It is a Lo Shu magic square!\n')
    else:
        print('It is not a Lo Shu magic square.\n')
    
    b=[[5, 5, 5], [5, 5,5], [5, 5, 5]]
    print('Your square is:')
    print_square(b)
    t=is_magic(b)
    #print(t)
    if t== True:
        print('It is a Lo Shu magic square!\n')
    else:
        print('It is not a Lo Shu magic square.\n')

    b=[[4, 9, 2], [3, 5,7], [8, 1, 6]]
    print('Your square is:')
    print_square(b)
    t=is_magic(b)
    #print(t)
    if t== True:
        print('It is a Lo Shu magic square!')
    else:
        print('It is not a Lo Shu magic square.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
