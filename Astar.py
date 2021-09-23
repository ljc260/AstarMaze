import maze as Maze
import math
import time

from colorama import init
from colorama import Fore, Back, Style
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.h = 0
        self.g = 0
        

    def __eq__(self, other):
        return self.position == other.position
    def __lt__(self, other):
        return self.f < other.f


def inOpenList(openList, neighbor):
    for point in openList:
        if(neighbor == point and neighbor >= point):
            return False
    return True

# manhattan distance
def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)
#  euclidean_distance
def euclidean_distance(point1, point2):
    xdist = point1[0] - point2[0]
    ydist = point1[1] - point2[1]
    return math.sqrt((xdist * xdist) + (ydist * ydist))

def educated_guess(point1, point2):
    xdist = (point1[0] - point2[0])
    ydist = (point1[1] - point2[1])

    return ((xdist**2)+(ydist**2)) 

def getheuristic(point1, point2, heuristictype):
    # manhattanDistance
    if heuristictype == 0:
        return heuristic(point1, point2)
    elif heuristictype == 1:  #eucliden distance
        return euclidean_distance(point1, point2)
    elif heuristictype == 2:  # educated guess
        return educated_guess(point1, point2)

# looks at all 4 adjacent locations around each point adds to neighbors if it is a 'c'
def getneighbors(currentpositionx, currentpositiony, maze):
    neighbors = []
    if maze[currentpositionx-1][currentpositiony] == 'c':
        neighbors.append((currentpositionx-1, currentpositiony))
    if maze[currentpositionx][currentpositiony - 1] == 'c':
        neighbors.append((currentpositionx, currentpositiony - 1))
    if maze[currentpositionx][currentpositiony + 1] == 'c':
        neighbors.append((currentpositionx, currentpositiony + 1))
    if maze[currentpositionx+1][currentpositiony] == 'c':
        neighbors.append((currentpositionx+1, currentpositiony))
    return neighbors
def getpath(currentNode):
    pathFound = []

    current = currentNode
    while current is not None:
        pathFound.append(current.position)
        current = current.parent
    # Return path reversed
    return pathFound[::-1] 

def astar(maze, start, end, heuristictype):
    
    startNode = Node(None, start)
    goalNode = Node(None, end)
    # startNode.f = heuristic(start, end)
    # create open and closed list
    openList = []
    visited = []
    openList.append(startNode)

    
    while len(openList) > 0:

        currentNode = openList[0]
        currentIndex = 0
        # if f score of node in open list < current node, than not searching current node 
        # and searching node with less weight
        for indexofnode, openlistnode in enumerate(openList):
            if openlistnode < currentNode:
                currentNode = openlistnode
                currentIndex = indexofnode

        openList.pop(currentIndex)
        visited.append(currentNode)

        # goal found
        if currentNode == goalNode:
            pathFound = getpath(currentNode)
            return pathFound

        # neighbors finds up, down, left, right only if they are c 
        neighbors = getneighbors(currentNode.position[0], currentNode.position[1], maze)
        for neighborposition in neighbors: 
            neighbor = Node(currentNode, neighborposition)

            # if neighbor already visited
            if neighbor in visited:
                continue
            
            point1 = (neighborposition[0], neighborposition[1])
            point2 = (goalNode.position[0], goalNode.position[1])
            #update values of the current neighbor
            neighbor.h = getheuristic(point1, point2, heuristictype)
            neighbor.g += 1
            neighbor.f = neighbor.g + neighbor.h

            # if in open list and if the fscore is greater than the current neighbor
            #  than false and wont be the shortest path
            if(inOpenList(openList, neighbor)):
                openList.append(neighbor)

    return None

# changes the maze based on path given from astar, visual purposes only
def changeMaze(maze, path):
    for point in path:
        maze[point[0]][point[1]] = 'p'


def main(height, width, heuristictype):
    mazeObj = Maze.Maze(int(height), int(width))

    maze = mazeObj.maze
    start = mazeObj.start_index
    end = mazeObj.end_index
    time.sleep(3)
    t0 = time.time()
    completedPath = astar(maze, start, end, heuristictype)
    t1 = time.time()
    overalltime = t1 - t0
    print("Solving...")
    #time.sleep(4)
    print(Fore.WHITE + str(completedPath), end='\n')
    changeMaze(maze, completedPath)
    print("The Path Taken...")
    time.sleep(3)
    mazeObj.printMaze(maze, mazeObj.height, mazeObj.width)
    #time.sleep(2)
    print("Time: " + str(overalltime) + " seconds")
    return overalltime
    


if __name__ == '__main__':
    overalltime = main(10, 25, 0)
   