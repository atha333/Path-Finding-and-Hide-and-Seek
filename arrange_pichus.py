#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#Assumptions: House is nxm matrix always. There is always one agent on the board to begin with.
# Submitted by : [Harsh Kirtikumar Atha] [User: hatha]
# Changes made: Created individual functions to store invalid spaces from rows, diagonals, anti diagonals and columns. Called them in successor
# function to remove those invalkid entries from positions you can use.
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
# Added a condition that calls condition_check to ensure invalid states are not selected.
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if (house_map[r][c] == '.')\
                                                                            and ((r,c) not in condition_check(house_map))]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Function combines lists obtained from rows, diagonals, columns and antidiagonals invalid positions/coordinates.
def condition_check(house_map):
    return column_invalid_list(house_map) + row_invalid_list(house_map)+diag_invalid_list(house_map)+adiag_invalid_list(house_map)


#First we find out the coordinates of agents on the map and store them. We create a list that stores unwanted coordinates.
#By traversing up and down the column where 'p' exists, we check if we find a wall/person. We store all '.' or empty spaces that occure
#immediately after the agent's position before a block/wall. 
def column_invalid_list(house_map):
    loc_p = [(row,col) for col in range(len(house_map[0])) for row in range(len(house_map)) if house_map[row][col]=="p"]
    
    row_count=len(house_map) #No of rows
    col_count=len(house_map[0]) #No of columns
    invalid_coord_in_columns=[]
    
    #Repeat for all positions of p
    for location in loc_p:    
        i=location[0] #iterator starting at r
        r=location[0] #row position for the agent
        c=location[1] #column position for the agent
        #Travel down the column from r to end of matrix
        while i<row_count-1:
            if house_map[i+1][c] in 'X@':
                break
            elif house_map[i+1][c]=='.':
                invalid_coord_in_columns.append((i+1,c))
            i+=1
        j=location[0] #row position for the agent
        
        #Travel up the column from r to 0
        while j>0:
            if house_map[j-1][c] in 'X@':
                break
            elif house_map[j-1][c]=='.':
                invalid_coord_in_columns.append((j-1,c))
            j-=1    
       
    return invalid_coord_in_columns

def row_invalid_list(house_map):
    loc_p = [(row,col) for col in range(len(house_map[0])) for row in range(len(house_map)) if house_map[row][col]=="p"]
    
    row_count=len(house_map) #No of rows
    col_count=len(house_map[0]) #No of columns
    invalid_coord_in_rows=[]
    
    #Repeat for all positions of p
    for location in loc_p:
        i=location[1] #iterator position starting at c
        r=location[0] #row position for the agent
        c=location[1] #column position for the agent
        
        #Traveling along the same row from c to last column.
        while i<col_count-1:
            if house_map[r][i+1] in 'X@':
                break
            elif house_map[r][i+1]=='.':
                invalid_coord_in_rows.append((r,i+1))
            i+=1
        j=location[1] #column position for the agent
        
        #Traveling along the same row from c to column 0.
        while j>0:
            if house_map[r][j-1] in 'X@':
                break
            elif house_map[r][j-1]=='.':
                invalid_coord_in_rows.append((r,j-1))
            j-=1
        
    return invalid_coord_in_rows
    

def diag_invalid_list(house_map):
    loc_p = [(row,col) for col in range(len(house_map[0])) for row in range(len(house_map)) if house_map[row][col]=="p"]
    row_count=len(house_map) #No of rows
    col_count=len(house_map[0]) #No of columns
    invalid_coord_in_diag=[]
    
    #Repeat for all positions of p
    for location in loc_p:
        i=location[0] #Iterator starting from r
        j=location[1] #Iterator starting from c
        r=location[0] #Row coordinate
        c=location[1] #Column coordinate
        
        #Travelling towards South east from (r,c)
        while ((i>0)and(j>0)):
            if house_map[i-1][j-1] in 'X@':
                break
            elif house_map[i-1][j-1] =='.':
                invalid_coord_in_diag.append((i-1,j-1))
            i-=1
            j-=1
        
        #Traveling towards #North west from (r,c)
        i=r #Reinitialize variable
        j=c #Reinitialize variable
        while ((j<col_count-1)and(i<row_count-1)):
            if house_map[i+1][j+1] in 'X@':
                break
            elif house_map[i+1][j+1] =='.':
                invalid_coord_in_diag.append((i+1,j+1))
            i+=1
            j+=1
                    
    return invalid_coord_in_diag

def adiag_invalid_list(house_map):
    loc_p = [(row,col) for col in range(len(house_map[0])) for row in range(len(house_map)) if house_map[row][col]=="p"]
    row_count=len(house_map) #No of rows
    col_count=len(house_map[0]) #No of columns
    invalid_coord_in_adiag=[]
    
    #Repeat for all positions of p
    for location in loc_p:
        i=location[0] #Iterator starting from r
        j=location[1] #Iterator starting from c
        r=location[0] #Row coordinate
        c=location[1] #Column coordinate
        
        #Traveling towards north east form (r,c)
        while ((i>0)and(j<col_count-1)):
            if house_map[i-1][j+1] in 'X@':
                break
            elif house_map[i-1][j+1] =='.':
                invalid_coord_in_adiag.append((i-1,j+1))
            i-=1
            j+=1
        
    
        i=r #Reinitialize variable
        j=c #Reinitialize variable
        #Traveling towards South West from (r,c)
        while ((i<row_count-1)and(j>0)):
            if house_map[i+1][j-1] in 'X@':
                break
            elif house_map[i+1][j-1] =='.':
                invalid_coord_in_adiag.append((i+1,j-1))
            i+=1
            j-=1
            
    return invalid_coord_in_adiag
        

        
    

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
# The solve function calls the successor and tries to obtain output by checking the conditions on next states. If goal of placing k number of agents
#is satisfied then it returns the new house map. Here I have added a list to maintain maps that have already been visited once in the successor.
#If there is any repeat then it will avoid visiting it. Added a check to return [], False if fringe has no data/states inside it.


def solve(initial_house_map,k):
    fringe = [initial_house_map]
    already_checked_states=[]
    while len(fringe) > 0:
        for new_house_map in successors(fringe.pop()):
            if new_house_map in already_checked_states:
# Used site https://www.geeksforgeeks.org/python-continue-statement/ to understand continue logic.
                continue
            already_checked_states.append(new_house_map)
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
    return ([],False)	

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


