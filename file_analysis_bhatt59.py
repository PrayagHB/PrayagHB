"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 09.4 - File Analysis  
Date: 03/24/2024

Description:
    This program compares the text in two text files and gives out the list of words for each files along with a list of common words and words not in common for both the files.

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
import string              # for importing punctuation string which contains a set of all the punctuation marks that we need to exclude
"""Write new functions below this line (starting with unit 4)."""
def main():
    #This program compares the text in two text files and gives out the list of words for each files along with a list of common words and words not in common for both the files.
    words_1 = []
    words_2 = []
    count_dict1={}
    count_dict2={}
    i=0
    l=0
    # for python_1 file
    with open("python_1.txt", 'r') as f:
        for line in f:
           for w in line.split():
                    clean_word =w.strip(string.punctuation)
                    words_1.append(clean_word.lower())
        s1=set(words_1)
        f1=list(sorted(s1))
        while i<len(f1):
            j=words_1.count(f1[i])
            count_dict1[f1[i]] = j
            i+=1
    with open("python_1_word_frequency.txt", 'w') as f:
        r1 = ''
        for key, value in count_dict1.items():
            r1 += f"{key}: {value}\n"
        f.write(r1)

     # for python_2 file
    with open("python_2.txt", 'r') as f:
        for line in f:
            for w in line.split():                 
                    clean_word =w.strip(string.punctuation)
                    words_2.append(clean_word.lower())
        s2=set(words_2)
        f2=list(sorted(s2))
        while l<len(f2):
            j=words_2.count(f2[l])
            count_dict2[f2[l]] = j
            l+=1
    with open("python_2_word_frequency.txt", 'w') as f:
        r2 = ''
        for key, value in count_dict2.items():
            r2 += f"{key}: {value}\n"
        f.write(r2)
    common=sorted(s1 & s2)
    with open("common_words.txt", 'w') as f:
        for word in common: 
            f.write(word + "\n")
    either_but_not_both=sorted(s1 ^ s2)
    with open("eitherbutnotboth.txt", 'w') as f:
        for word in either_but_not_both: 
            f.write(word + "\n")
            

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
