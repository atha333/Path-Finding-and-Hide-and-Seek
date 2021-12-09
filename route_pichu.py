#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
# There is one agent and one goal state. The goal state is known.
# Submitted by : [Harsh Kirtikumar Atha] [User name: hatha]
# Changes to skeleton code: 1. Addition of direction in moves function so both moves and direction get updated together. 
#                           2. Created a function to find manhattan distance between two points and use that as a heuristic function.
#                           3. Updated fringe with heuristic priority value, location, direction and cost/length of path.
#                           4. Created a check to ensure the agent doesn't go in an infinite loop by storing already visited states. 
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys
from queue import PriorityQueue

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
#Referred https://www.askpython.com/python/list/python-list-of-tuples to clarify tuples and lists.
def moves(map, row, col, direct):
        moves = ((row+1,col, direct + ['D']), (row-1,col,direct + ['U']), (row,col-1,direct + ['L']), (row,col+1,direct + ['R']))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)


#Referred https://stackoverflow.com/questions/16318757/calculating-manhattan-distance-in-python-in-an-8-puzzle-game for formula of Manhattan Distance
def manhattanDist(X,Y):
    distance = abs(X[0] - Y[0]) + abs(X[1] - Y[1])      
    return distance

def search(house_map):
        
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        goal_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="@"][0]
        
        direct = []
        already_visited =[pichu_loc]

    

# Used to understand how to get, put and put Priority, Element pair in PQ from https://www.educative.io/edpresso/what-is-the-python-priority-queue
        fringe = PriorityQueue()
        fringe.put((manhattanDist(pichu_loc,goal_loc), [pichu_loc,direct, 0]))
        
        while not fringe.empty():

            (heuristic_value, [current_move, direction, current_distance]) = fringe.get()

            for move in moves(house_map, current_move[0], current_move[1], direction):
                    if(house_map[move[0]][move[1]]=="@"):
                        
# Referred to https://www.geeksforgeeks.org/python-merge-list-elements/ for understanding how to merge elements of list  
                      
                         return (current_distance+1, "".join(move[2]))  
                    else:
                        if ((move[0],move[1]) not in already_visited):
                            already_visited.append((move[0],move[1]))
#Referred https://www.askpython.com/python/list/python-list-of-tuples to clarify tuples and lists.
#move[0] corresponds to row, move[1] corresponds to column position of the node. move[2] is the direction (L,U,D,R) being stored. 
                           
                            fringe.put(((manhattanDist(move,goal_loc)+current_distance+1), [(move[0],move[1]), move[2], current_distance+1]))
                          
        return -1                
                    
                    
          

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        if solution!=-1:
            print(str(solution[0]) + " " + solution[1])
        else:
            print(-1)

        
        
