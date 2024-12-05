# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
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


def graph_search(problem, pending_nodes):
    """
    A generalized graph search algorithm that works with different data structures.
    pending_nodes: A data structure (Stack for DFS, Queue for BFS) to manage exploration
    --------------------------------------------------
    problem.getStartState() --> (34,16)
    problem.isGoalState(problem.getStartState()) --> bool
    problem.getSuccessors(problem.getStartState()) --> [((34,15),'South', 1),((33,16),'West', 1)]
    """
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    pending_nodes.push((start_state, []))
    expanded_nodes = set()

    while not pending_nodes.isEmpty():
        current_state, actions = pending_nodes.pop()

        if current_state in expanded_nodes:
            continue

        expanded_nodes.add(current_state)

        if problem.isGoalState(current_state):
            return actions

        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in expanded_nodes:
                pending_nodes.push((successor, actions + [action]))

    raise Exception("No solution")


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    return graph_search(problem, util.Stack())


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    return graph_search(problem, util.Queue())


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    pending_nodes = util.PriorityQueue()
    start_state = problem.getStartState()

    if problem.isGoalState(start_state):
        return []

    pending_nodes.push((start_state, [], 0), 0)
    expanded_nodes = set()

    while not pending_nodes.isEmpty():
        current_state, actions, current_cost = pending_nodes.pop()

        if current_state in expanded_nodes:
            continue

        expanded_nodes.add(current_state)

        if problem.isGoalState(current_state):
            return actions

        for child, action, step_cost in problem.getSuccessors(current_state):
            if child not in expanded_nodes:
                total_cost = current_cost + step_cost
                pending_nodes.push((child, actions + [action], total_cost), total_cost)

    raise Exception("No solution found")


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    pending_nodes = util.PriorityQueue()
    start_state = problem.getStartState()

    if problem.isGoalState(start_state):
        return []
    pending_nodes.push((start_state, [], 0), 0 + heuristic(start_state, problem))
    expanded_nodes = set()

    while not pending_nodes.isEmpty():
        current_state, actions, current_cost = pending_nodes.pop()

        if current_state in expanded_nodes:
            continue

        expanded_nodes.add(current_state)

        if problem.isGoalState(current_state):
            return actions

        for child, action, step_cost in problem.getSuccessors(current_state):
            if child not in expanded_nodes:
                total_cost = current_cost + step_cost
                priority = total_cost + heuristic(child, problem)
                pending_nodes.push((child, actions + [action], total_cost), priority)

    raise Exception("No solution found")



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
