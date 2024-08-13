"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 08.2 - File Stats
Date: 03/11/2024

Description:
    This program gives data about the number of words and number lines in the file.

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
    #This program gives data about the number of words and number lines in the file.
    c = 0
    line_count = 0
    total_words_per_line = 0
    non_blank_lines = 0

    with open("frontiero_v_richardson.txt", 'r') as f:
        for line in f:
            line = line.strip()
            if line:                                    # Check if the line is non-blank
                words = line.split()
                c += len(words)
                total_words_per_line += len(words)
                non_blank_lines += 1

    if non_blank_lines != 0:
        avg_words = total_words_per_line / non_blank_lines
    else:
        avg_words = 0

    print(f"Total number of words: {c}")
    print(f"Total number of lines: {non_blank_lines}")
    print(f"Average number of words per line: {avg_words:.1f}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
