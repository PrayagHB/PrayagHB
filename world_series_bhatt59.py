"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 09.2 - World Series 
Date: 03/22/2024

Description:
    This program asks the user about the year and gives information about the team which won the world series (for years from 1903 to 2022).

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
def load_winners_data():
        count_dict={}
        year_dict={}
        l=[]
        i=0
        y=1903
        with open("WorldSeriesWinners.txt") as f:
            for line in f:
                parts = line.strip()
                l.append(parts)
            s=set(l)
            fl=list(s)
            while i<len(fl):
                j=l.count(fl[i])
                count_dict[fl[i]] = j
                i+=1
            i=0
            while i<len(l):
                if y==1904 or y==1994:
                    y+=1
                    year_dict[y] = l[i]
                    y+=1
                else:
                    year_dict[y] = l[i]
                    y+=1
                i+=1
            return count_dict,year_dict

def main():
    #This program asks the user about the year and gives information about the team which won the world series (for years from 1903 to 2022).
    k,p=load_winners_data()
    i=int(input('Enter a year in the range 1903 -- 2022: '))
    if i<1903 or i>2022:
        print(f'  Data for the year {i} is not included in this system.')
    elif i==1904 or i==1994:
        print(f"  The World Series wasn't played in the year {i}.")
    else:
        n=p.get(i)
        m=k.get(n)
        print(f'  The {n} won the World Series in {i}.')
        print(f'  They have won the World Series {m} times.')
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
