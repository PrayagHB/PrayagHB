"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 08.5 - Number Reader  
Date: 03/11/2024

Description:
    This program captures the input from the file created in the number_writer program and than calculates Min, Max, Sum and Avg.

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
    #This program captures the input from the file created in the number_writer program and than calculates Min, Max, Sum and Avg.
    with open("random_numbers.txt") as f:
        l=f.read()
        k=l.split('\n')
        del k[-1]
        k = list(map(int, k))  # Convert the list of strings to a list of integers
        min_num = min(k)  # Calculate the minimum value
        max_num = max(k)  # Calculate the maximum value
        total_sum = sum(k)  # Calculate the sum of all elements
        avg = total_sum / len(k)  # Calculate the average
        print(f'{len(k):,} numbers were read from the file.')
        print(f'Min: {min_num:,}')
        print(f'Max: {max_num:,}')
        print(f'Sum: {total_sum:,}')
        print(f'Avg: {avg:,.1f}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
