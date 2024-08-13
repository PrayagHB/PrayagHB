"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 08.2 - Step Counter
Date: 03/11/2024

Description:
    This program returns the average number of steps for each month walked for an entire year.

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
    #This program returns the average number of steps for each month walked for an entire year.
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    d=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",]
    print('The average steps taken each month were:')
    with open("steps.txt") as f:
        w=f.read()
        k=w.split('\n')
        c=j=0
        while c< len(m):
            i=0
            sum=0
            while i<int(m[c]):
                sum+=int(k[j])
                i+=1
                j+=1
            avg=sum/i
            p=d[c]
            print(f'{p.rjust(10)} : {avg:8.2f}')
            c+=1


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
