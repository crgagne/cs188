# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import pdb
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def actions_for_path(problem,path):
    """
    Find the actions to follow a certain path.

    Inputs a problem, which has getsuccessor, and a list of states (ie. path)

    Returns a list of actions
    """
    actions = []
    for i,node in enumerate(path):
        if i==(len(path)-1):
            break
        successors = problem.getSuccessors(node)
        for successor in successors:
            ss,aa,_ = successor
            if ss == path[i+1]:
                actions.append(aa)
                break
    return(actions)

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # current path stack
    path_stack = util.Stack()
    action_stack = util.Stack()
    path_stack.push(problem.getStartState())

    # visited (so don't )
    visited = []
    visited.append(problem.getStartState())

    i = 0
    while not path_stack.isEmpty():

        # check goal state
        if problem.isGoalState(path_stack.list[-1]): # check if goal
            return action_stack.list

        # get next possible state (choose first in list)
        successors = problem.getSuccessors(path_stack.list[-1])
        forward=False
        for successor in successors:
            ss,aa,_ = successor
            if ss not in visited:

                path_stack.push(ss)
                action_stack.push(aa)
                visited.append(ss) # you don't pop visited
                forward=True
                break

        # backtrack
        if forward==False:
            path_stack.pop()
            action_stack.pop()

        i+=1
        #if i==25:
        #    import pdb; pdb.set_trace()
        #print(path_stack.list)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # fringe priority queue
    fringe = util.PriorityQueue()
    fringe.push([problem.getStartState()],1) # fringe will have (priority, order, [s0,s1,..])

    # closed set
    closed = []

    i = 0
    while not fringe.isEmpty():

        # get highest priority path for expansion e.g. [s0,s2,s4]
        path_exp = fringe.pop()

        # take last node in path e.g. s4
        node_exp = path_exp[-1]

        # check goal state
        if problem.isGoalState(node_exp): # check if goal
            actions = actions_for_path(problem,path_exp)
            #import pdb; pdb.set_trace()
            return actions

        # add expanded node into closed set e.g. [s0,s1,s2]
        if node_exp not in closed:
            closed.append(node_exp)
        else:
            # if it's in the closed set, don't expand
            continue

        # get sucessors to expand fringe
        successors = problem.getSuccessors(node_exp)
        for successor in successors:
            # unpack states, actions
            ss,aa,_ = successor
            if ss not in closed:
                path = path_exp+[ss]
                # expand fringe by adding candidate paths, prioritize by len of path
                fringe.push(path,len(path))

        #i+=1
        if i==1000:
            import pdb; pdb.set_trace()

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
