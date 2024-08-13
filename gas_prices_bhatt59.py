"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 03/25/2024

Description:
    This program plots a line graph for the average gasoline price in US for year 2008.

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""
     

def main():
    #This program plots a line graph for the average gasoline price in US for year 2008.
    l=[]
    weeks = []
    for i in range(1, 53):
        weeks.append(i)
    with open("2008_Weekly_Gas_Averages.txt", 'r') as f:
        k=f.readlines()
        for i in k:
            #j=i.strip('\n')
            l.append(float(i))
        fig, ax = plt.subplots()
        y = l
        x= weeks
        ax.plot(x,y)
        ax.set_title('2008 Weekly Gas Prices (bhatt59)')
        ax.set_xlabel('Weeks (by number)')
        ax.set_ylabel('Average Price (dollars/gallon)')
        ax.set_xlim(1, 52)
        ax.set_ylim(1.5, 4.25)
        ax.set_xticks([10,20,30,40,50])
        ax.set_yticks([1.5,2.0,2.5,3.0,3.5,4.0])
        ax.grid()
        plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
