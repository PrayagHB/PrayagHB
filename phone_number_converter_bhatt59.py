"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 03/07/2024

Description:
    This program converts alphabetic number into a phone number by replacing the alphabets with numbers.

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
def convert_number(a:str):
    p=[]
    for j in a:
        if 'A' <= j <='C' or 'a' <= j <='c':
            p.append('2')
        elif 'D' <= j <='F' or 'd' <= j <='f':
            p.append('3')
        elif 'G' <= j <='I' or 'g' <= j <='i':
            p.append('4')
        elif 'J' <= j <='L' or 'j' <= j <='l':
            p.append('5')
        elif 'M' <= j <='O' or 'm' <= j <='o':
            p.append('6')
        elif 'P' <= j <='S' or 'p' <= j <='s':
            p.append('7')
        elif 'T' <= j <='V' or 't' <= j <='v':
            p.append('8')
        elif 'W' <= j <='Z' or 'w' <= j <='z':
            p.append('9')
        else:
            p.append(j)
    return ''.join(p)
    

def main():
    #This program converts alphabetic number into a phone number by replacing the alphabets with numbers.
    a=str(input('Enter a telephone number: '))
    print(f'  {a}')
    o=convert_number(a)
    print(f'  {o}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
