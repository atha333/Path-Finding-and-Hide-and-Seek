# CS B551 FA2021 Assignment 0

## Part 1: Navigation

The goal of this assignment is to find an optimal path for the agent (pichu) to move from it's current position to the goal state. The house is an NxM matrix where p is the agent and @ is the goal. X denotes walls/blocks in the way. Figure below represents an example of the map.
Assumptions: There is always exactly one 'p' and one '@' in the map file.  If there is no solution, the program displays -1 as the length.

![image](https://media.github.iu.edu/user/18130/files/43857200-17d3-11ec-89f7-3bf9d77f3aac)



Output should be of the form:

Shhhh... quiet while I navigate!
Here’s the solution I found:
16 UUURRDDDRRUURRDD

## Problems in existing skeletal code:

a. The given skeletal code does not have an exit condition in case there is no output.

b. There is no variable/data structure to determine the path taken by pichu.

c. The code gets stuck in an infinite loop.

## All 3 problems are solved in the code here. 
## Search Abstraction:

1. Set of States S: It can be defined as a set of all legal moves that can be reached from your initial state.
2. Successor function: It returns the immediate neighbour in Up, down, left or right direction. It is bound by some constraints like the agent only moving along X or Y axis and                        not diagonally. It also cannot be on same node as X, travel via X or @.
3. Initial State: The initial state is pichu at position p and human at @. The house where goal is yet to rach is the board before the start of the game if we talk in a gamer                     sense.
4. Goal State: To reach destination (@).
5. Cost = Distance travelled by pichu from p to @.


## Approaches:

A) Initially I tried to modify the existing algorithm directly by introducing 3 major changes. The first was that the code got stuck in an infinite loop. Using the logic of storing states/nodes already visited by pichu we can ensure that it doesnt get stuck in infinity and will not go back to a visited node. An exit condition was also added in search function to return -1 as output if there's no possible output. Last but not the least, a variable(list) was created to store the directions pichu has taken to reach the goal.

B) This is the approach currently being used in the code of route_pichu.py. To ensure that the search for an optimal solution is not done in the entire sample set, I used a heuristic function. It gave out the Manhattan Distance between the current state and goal added by the cost it took to travel there. This was done using a priority queue that ensures that only moves with highest priority (lowest Manhattan distance+cost of moves) were first checked out. The other issues of infinite loop and the lack of directions/exit condition were done using the same logic as above.

C) Another method I tried to consider was parallelly checking the path in a bidirectional way. Path travelled by pichu towards the goal would be stored in a data structure like list and another backtracking path would be derived parallelly from goal towards starting point. When both the lists have one common point, it would ensure that they have met and that can be considered the optimal solution. I was unable to do this as I don't have prior knowledge of working with parallel computing and was unsure on how to exit the loop when both paths meet at one point.


The code gave correct outputs for given test cases as well as an array of other custom test cases.

### References used for Python operations (mentioned in code as well):
1. https://stackoverflow.com/questions/16318757/calculating-manhattan-distance-in-python-in-an-8-puzzle-game for formula of Manhattan Distance.
2. Used to understand how to get, put and put Priority, Element pair in PQ from https://www.educative.io/edpresso/what-is-the-python-priority-queue
3. Referred to https://www.geeksforgeeks.org/python-merge-list-elements/ for understanding how to merge elements of list 



# Part 2: Hide-and-seek


There are k agents in the house where k>=1. Assume two agents can see each other if they are on either the same row, column, or diagonalof the map, and there are no walls between them. The goal is to place k agents on the board such that they do not face each other. They can be blocked by a wall, person (@). Assumption made is that the house is an nxm matrix and there is atleast one agent placed on the board to begin with. The house/output would look like a below example:

![image](https://media.github.iu.edu/user/18130/files/5bf58c80-17d3-11ec-9f42-83a0d02c66bb)


A logic had to be implemented to set the agents in best possible positions so that they are not in line of sight of other agents. This problem is similar to N Queens problem except for addition of walls in between.

## Search Abstraction:

1. Set of States S: S can be defined as all states where the agent is in a blank spot such that there is no other agent in same row, column, diagonals, anti-diagonals.
2. Successor Function: It gives out list of all possibilities where an agent exists on blank spot where it doesn't break the rule of peeking at another agent.
3. Initial State: A house map where there is atleast one agent placed with existing walls and 1 human.
4. Goal State: While ensuring that the given conditions are followed, the program should return a map placing n agents correctly in place or return False where no solution exists.
5. The cost here depends on the time the program takes to place k agents on a nxm board.

## Approaches used:

A) In my first approach I planned to traverse entire rows, columns, diagonals and anti-diagonals. When going down a column from index 0 to m-1, my algorithm kept a count of no of agents detected. If the count(agent) =1 and then a wall was found as we moved down the count was changed to 0. If at any given time the count became 2, it would exit the loop and the position/state of the board at that given time would be considered invalid. Maintaining these counts proved to be a bit difficult for me in cases where we iterate to the last column/row and there is either a combination of walls/no agents. This approach was discarded for another one as below.

B) I planned to first find poitions of current agents and then using individual functions for row, column, diagonals and anti-diagonals, the program stored states that are invalid. If there is a blank space('.') just immediately after 'p', it becomes an invalid place to add another 'p'. This mapping was done for all possible values of 'p' found in successor states. In case where next value of 'p' does not lie in these coordinates, it was considered as valid. Once successor generates the next state, we check if that has already been visited. If that is true then we skip the step, else we store that in a list to avoid infinite loop problems. I added a check to see if the function returned None, it will give a reply as False.

The code gave correct outputs for given test cases as well as an array of other custom test cases.

### References:

http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html

https://www.geeksforgeeks.org/python-continue-statement/











