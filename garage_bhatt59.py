"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 11.2 - Garage
Date: 04/02/2024

Description:
    This program defines a class Garage and uses this to make a garage manager which gives information about how many cars and empty spaces are available.

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
class Garage:
        def __init__(self,name,spaces,cars):
            self.name=name
            self.spaces=spaces
            self.cars=cars
        def car_in(self):
            if self.cars>=self.spaces:
                return print(f'  Lot {self.name} is full. Can not add another car.')
            else: 
                self.cars+=1
                return print(f'  Added a car to Lot {self.name}')
        def car_out(self):
            if self.cars==0:
                return print(f'  Lot {self.name} is empty. There are no cars to remove.')
            else: 
                self.cars-=1
                return print(f'  Removed a car from Lot {self.name}')
        def status(self):
            k=self.spaces-self.cars
            return print(f'  Lot {self.name}: {k} out of {self.spaces} spaces are available.')
              
        

def main():
    #This program defines a class Garage and uses this to make a garage manager which gives information about how many cars and empty spaces are available.
    print(f'Welcome to the Garage Manager!\n------------ Menu ------------\n  0. Exit\n  1. Print current status.\n  2. Add a car to A lot.\n  3. Add a car to B lot.\n  4. Remove a car from A lot.\n  5. Remove a car from B lot.')
    i= Garage('A',10,8)
    f= Garage('B',15,1)
    while True:
        x = int(input('Please choose an option (0-5): '))
        if x == 0:
            break
        elif x == 1:
            print('Current Garage Status:')
            i.status()
            f.status()
        elif x == 2:
            i.car_in()
        elif x == 3:
            f.car_in()
        elif x == 4:
            i.car_out()
        elif x == 5:
            f.car_out()
    print('End of the Day Garage Status:')
    i.status()
    f.status()
        
    
            


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
