"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 02.4 -  Time Calculator 
Date: 01/27/2024

Description:
    This program converts the number of seconds entered by the user into time in format of Days,Hours,Minutes and Seconds.

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
    #This program converts the number of seconds entered by the user into time in format of Days,Hours,Minutes and Seconds.
    x=int(input("Please enter a time in seconds: "))
    if x<60:
        print(f"  {x:,d} seconds is less than one minute.")
    else:
        d=x//86400
        h=x%86400//3600
        m=x%3600//60
        s=x%60
        print(f'  {x:,d} seconds equals ', end = '') 
        if d:
            print(f'{d} day(s)', end = '')
            if h:
                if m:
                    print(', ', end = '')
                elif s:
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            elif m:
                if s:
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            elif s:
                print(' and ', end = '')

        if h:
            print(f'{h} hour(s)', end = '')
            if d:                               #this condition check is extra because the requirement was to put comma before 'and' when we have a combination of 3 or all 4 entities for eg- d,h,m,And s  or d,m,and s
                if m:
                    if s:
                        print(', ', end = '')
                    else:
                        print(', and ', end = '')
                elif s:
                    print(', and ', end = '')
            else:
                if m:
                    if s:
                        print(', ', end = '')
                    else:
                        print(' and ', end = '')
                elif m:
                    print(' and ', end = '')
                elif s:
                    print(' and ', end = '')

        if m:
            print(f'{m} minute(s)', end = '')
            if d or h:                            #this condition check is extra because the requirement was to put comma before 'and' when we have a combination of 3 or all 4 entities for eg- d,h,m,And s  or d,m,and s
                if s:
                    print(', and ', end = '')
            else:
                if s:
                    print(' and ', end = '')
                            
        if s:
            print(f'{s} second(s)', end = '')
        print('.')
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
