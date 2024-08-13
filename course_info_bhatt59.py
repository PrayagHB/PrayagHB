"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 09.3 - Course Info
Date: 03/22/2024

Description:
    This program provides the details about the course based on the course number entered by the user.

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
def get_course_data():
    d={}
    d={'CS101':{'room':'1461','instructor':'Django','time':'9:00 a.m.'},
       'CS102':{'room':'4815','instructor':'Idle','time':'11:00 a.m.'},
       'CS103':{'room':'3634','instructor':'Rich','time':'10:00 a.m.'},
       'NT110':{'room':'1188','instructor':'Marshal','time':'2:00 p.m.'},
       'CM241':{'room':'2451','instructor':'Pickle','time':'12:00 p.m.'}}
    return d

def main():
    #This program provides the details about the course based on the course number entered by the user.
    k=get_course_data()
    i=str(input('Enter a course number: '))
    if i in k:
        print(f'  The details for course {i} are:')
        r=k[i]['room']
        n=k[i]['instructor']
        t=k[i]['time']
        print(f'    Instructor: {n}\n          Room: {r}\n          Time: {t}')
    else:
        print(f'  {i} is an invalid course number.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
