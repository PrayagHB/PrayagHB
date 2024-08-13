"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 10.4 - Function Plot
Date: 03/27/2024

Description:
    This program captures the input from user in pig latin and then translates it into a normal sentence.

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
import math as m


"""Write new functions below this line (starting with unit 4)."""


def main():
    #This program captures the input from user in pig latin and then translates it into a normal sentence.
    sinf=[]
    cosf=[]
    v=[]
    for i in range(0,int(2.1*m.pi*100),1):
        i=i/100
        f1=float(((5*m.sin(i))**2)-10)
        f2=float((10 * m.cos(i ** 2)) + (i ** 2) - 20) 
        sinf.append(f1)
        cosf.append(f2)
        v.append(i)
    fig, ax = plt.subplots()
    y1=sinf
    y2=cosf
    x=v
    ax.plot(x,y1,color='g')
    ax.plot(x,y2,color='b')
    ax.set_title('10.4 Function Plot (bhatt59)')
    ax.set_xlim(0, 2.01*m.pi)
    ax.set_ylim(-30, 30)
    ax.set_xticks([m.pi / 2, m.pi, 3 * m.pi / 2, 2 * m.pi])
    ax.set_xticklabels([r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
    ax.set_yticks([-20,-10,10,20])
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
    ax.legend([r"$(5\sin{x})^2 - 10$", r"$10\cos{(x^2)} + x^2 - 20$"], loc='lower right')
    plt.show()



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
