"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 11.3 - Rockets
Date: 04/02/2024

Description:
    This program uses the class Rocket and subclass ReusableRockets to print the total cost of launching the rocket.

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
class Rocket:
    def __init__(self,name,booster_cost,upper_stage_cost,fuel_cost):
        self.booster_cost=booster_cost
        self.upper_stage_cost=upper_stage_cost
        self.fuel_cost=fuel_cost
        self.name=name
    def cost_per_launch(self):
        c=self.booster_cost+self.upper_stage_cost+self.fuel_cost
        return print(f'This {self.name} cost ${c:.2f} million per launch.')
        
class ReusableRocket(Rocket):
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost, uses):
        super().__init__(name, booster_cost, upper_stage_cost, fuel_cost)
        self.uses = uses
    def cost_per_launch(self):
        c=(self.booster_cost/self.uses)+self.upper_stage_cost+self.fuel_cost
        return print(f'This {self.name} cost ${c:.2f} million per launch.')
        

def main():
    #This program uses the class Rocket and subclass ReusableRockets to print the total cost of launching the rocket.
    a=Rocket('Atlas V',65.4,42.6,0.23)
    b=Rocket('Ariane 5',83.5,55.6,0.69)
    c=Rocket('Long March 3B',28.5,19.0,2.38)
    d=Rocket('Soyuz 2',20.9,13.9,0.24)
    e=ReusableRocket('Falcon 9',43.0,18.6,0.45,20)
    a.cost_per_launch()
    b.cost_per_launch()
    c.cost_per_launch()
    d.cost_per_launch()
    e.cost_per_launch()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
