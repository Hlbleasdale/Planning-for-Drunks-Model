# Import relevant libraries 
import random # used for generating psuedo-random numbers 
import itertools # used to assign each agent their house number 

# Set up a class for Drunks 

class Drunks():
    
    # Use the intertools count function to set the drunk agents house
    # numbers as multiples of 10, starting from 10
    house_number = itertools.count(10, 10)
    
    # use the __init__ method to construct the class with attributes
    # of the agents, including a house number
    def __init__(self, town, drunks, pubx, puby, density):
        
        # Assign each drunk agent a house number using the itertools
        # function created above (house_number)
        self.house = int(next(self.house_number))
        
        # Assign the agents to the town, where they shall roam around, 
        # and can not go past the town boundary
        self.town = town
        
        # 
        self.drunks = drunks
        
        # Set up two coordinates for the pub location, where all of the
        # agents will start
        self.x = pubx
        self.y = puby
        
        # Set up an attribute to recognise if the drunk agent has 
        # already been in a certain cell to stop the drunks retracing
        # their steps
        self.visited = {(self.x, self.y)}
        
        # Set up an attribute, density, to record where the agents have been
        # to plot this on a density map
        self.density = density
    
    # Move the agents with a conditional statement
    # use self.visited to ensure the agents can not retrace their 
    # steps by entering a cell they have already entered
    def move(self, town):
    
        while (self.x, self.y) in self.visited:
            try_again = True
            while try_again:
                    # Move the agents one step depending on the outcome of the
                    # random number generator
                    # the agents can only move within the boundary of the town
                    if random.random() < 0.5:
                        next_x = (self.x + 1) % len(self.town [0])
                    else:
                        next_x = (self.x - 1) % len(self.town [0])
                        
                    if random.random() < 0.5:
                        next_y = (self.y + 1) % len(self.town)
                    else: 
                        next_y = (self.y - 1) % len(self.town)
                    
                    if  self.town[next_x][next_y] == 0 or \
                        self.town[next_x][next_y] == self.house:
                        self.x = next_x
                        self.y = next_y
                        try_again = False
        self.visited.add((self.x, self.y))  
        
    # Set up a function to record the density of agents in the cells
    def steps (self, density):
        self.density [self.x][self.y] +=1 
