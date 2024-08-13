"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 10.1 - Monthly Sales 
Date: 03/25/2024

Description:
    This program captures the input from user for monthly sales in a single year and plots a pie chart for the same with a given combination of colors.

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
    #This program captures the input from user for monthly sales in a single year and plots a pie chart for the same with a given combination of colors.
    month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    l=[]
    for i in month:
        k=str(input(f'Enter the sales for {i}: '))
        l.append(k)
    fig, ax = plt.subplots()
    y = l
    la = ['January','February','March','April','May','June','July','August','September','October','November','December']
    c=('#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A','#FFD100','#29A592')
    ax.pie(y,colors=c,labels=la)
    ax.set_title('Monthly Sales Values (bhatt759)')
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
