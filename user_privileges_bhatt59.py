"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 11.5 - User Privileges
Date: 04/03/2024

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


"""Write new functions below this line (starting with unit 4)."""
class Privileges:
    def __init__(self, privs={'interact', 'post'}):
        self.privs = set(privs)
    def grant(self, priv):
        self.privs.add(priv)
        return print(f"Granted {priv}")
    def revoke(self, priv):
        self.privs.remove(priv)
        return print(f"Revoked {priv}")
    def get_privs(self):
        return ', '.join(sorted(self.privs))
        
class User:
    def __init__(self, name, email):
        #super().__init__() 
        self.name = name
        self.email = email
        self.privs= Privileges()
    def describe_user(self):
        print('User Profile')
        print(f"  Name: {self.name}")
        print(f"  Email: {self.email}")
        print(f"  Privs: {self.privs.get_privs()}")


def main():
    #This program captures the input from user in pig latin and then translates it into a normal sentence.
    k = User('Alice', 'alice@example.com')
    k.describe_user()
    k.privs.grant('teleport')
    k.describe_user()
    k.privs.revoke('post')
    k.describe_user()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
