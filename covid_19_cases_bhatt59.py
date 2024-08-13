"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 10.3 - covid 19 cases
Date: 04/01/2024

Description:
    This program utilizes the data for the covid cases in Indiana state and plots an incremental bar graph denoting the total cases for the week.

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
import datetime


"""Write new functions below this line (starting with unit 4)."""

        

def main():
    #This program utilizes the data for the covid cases in Indiana state and plots an incremental bar graph denoting the total cases for the week.
    date=[]
    cases=[]
    total_cases=[]
    j=2
    with open("indiana_covid-19_data_spring_2023.txt", 'r') as f:
        for line in f:
            k=line.split()
            date.append(k[0])
            cases.append(float(k[2]))
            total_cases.append((sum(cases))/1000)
        t = []
        for dat in date:
            y, m, d = dat.split('-')
            dt = datetime.date(int(y), int(m), int(d))
            t.append(dt)
        fig, ax = plt.subplots()
        y = total_cases
        x= t
        ax.bar(x,y,width=7)
        fig.autofmt_xdate()
        ax.set_title('Weekly Positive COVID-19 Cases in Indiana (bhatt59)')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Cases (in thousands)')
        ax.set_xlim(datetime.datetime(2019, 12, 16), datetime.datetime(2023, 5, 16))
        ax.set_ylim(0, 2250)
        ax.set_yticks([0,250,500,750,1000,1250,1500,1750,2000,2250])
        plt.show()
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
