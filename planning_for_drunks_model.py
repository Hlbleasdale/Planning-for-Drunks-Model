# Import relevant libraries 

# Import agents class containing functions and attributes of the agents
import drunkagents 
# Import matplotlib for plotting the model
import matplotlib.pyplot as plt
# Import csv to read in the raster file representing the pub point and houses
import csv 
            
# Set up the variables 
# Set up the total number of drunk people (25)
num_of_agents = 25
# Set up an empty list, density, which will hold the record of the agents routes
density = []
# Set up an empty list, town, so the town file can be read into it
town = []
# Set up an empty variable, drunks, where the drunk agents can be appended to 
# from the drunkagents framework
drunks = []

# Set up the location of the pub 
pubx, puby = 0,0

# Read in the txt file using relevant file path
with open ('drunk.plan.txt') as inp_file:
    reader = csv.reader(inp_file, quoting=csv.QUOTE_NONNUMERIC)
    # Create a for loop to make each row a list in the town,
    # with each row being filled with values 
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(int(value))
        town.append(rowlist)

# Read in the text file again, this time making the values of each row
# of the town empty to enable addition of the density of each point (the
# number of drunk agents passing through each cell)
with open ('drunk.plan.txt') as inp_file:
    reader = csv.reader(inp_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            value = 0
            rowlist.append(int(value))
        density.append(rowlist)

# Locate the pub so it can be used as a starting point for the agents 
for j, row in enumerate(town):
    for i, num in enumerate(row):
        # the pub is denoted by 1
        if num == 1:
            pubx,puby = i,j
                        
# Create the drunk agents, using the imported drunkagents and append them to 
# the town
for i in range(num_of_agents):
    drunks.append(drunkagents.Drunks(town, drunks, pubx, puby, density))
    # Check the drunks have got houses from 10-250
    print(drunks[i].house)
    
# Create a for loop to move the agents and to trace the agents steps and record
# this in the density variable
# Create a variable, total, with an initial value of 0, where the amount of 
# drunks who have made it home shall be recorded
total = 0
for i in range(num_of_agents):
    # While the drunks are not at home,
    while (town[drunks[i].x][drunks[i].y] != drunks[i].house):
        # move the agents (using move function from drunkagents class)
        drunks[i].move(town)
        # record the steps of the agents in the density variable
        drunks[i].steps(density)
   # if the drunks have reached their house     
    else:
        # Add one to the total
        total += 1
        # Check this works by printing
        print("Amount of drunks who have reached home is", total)
        # If all of the agents reach home, print "all drunks are home safe"
        if total == (num_of_agents):
            print("All drunks are home safe!")

# Plot the town, the agents and the pub
plt.xlim(0, len(town [0]))
plt.ylim(0, len(town))
# Plot the density to visibly show the routes the agents have taken to get home
plt.imshow(density)

# Export the density file as a txt file 
with open('density.txt', 'w', newline='') as out_file:
    writer = csv.writer(out_file, delimiter=',')
    for row in density:
        writer.writerow(row)
        