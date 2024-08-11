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


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    stack = util.Stack() #καθε στοιχειο του στακ θα αποτελειτσαι απο το ενα state και το μονοπατι απο το starting state για να φτασει στο current_state
    visited_states = set()
    starting_state = problem.getStartState()
    root_from_starting_state = [] #καθε state(κομβος του δεντρου) θα εχει και μια λιστα απο τις κινησεις που εγιναν για να φταση εκει 

    stack.push((starting_state, root_from_starting_state)) #το μονοπατι απο το starting_state προς το starting_state ειναι προφανως η κενη λιστα

    while True:

        if stack.isEmpty(): #base case1
            return []
        
        stacks_elements = stack.pop()
        current_state = stacks_elements[0]
        visited_states.add(current_state)
        root_to_current_state = stacks_elements[1]

        if problem.isGoalState(current_state): 
            return root_to_current_state

        successors = problem.getSuccessors(current_state)
        if len(successors) != 0: #ελεγχω αν υπαρχουν current state successors
            for element in successors:
                next_state = element[0]
                if next_state not in visited_states:
                    root_to_next_state = root_to_current_state #το μονοπατι μεχρι να φτασουμε στο current state
                    root_to_next_state = root_to_next_state + [ element[1] ] # συν το επομενο βημα
                    stack.push((next_state, root_to_next_state))

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    
    queue = util.Queue() #καθε στοιχειο του στακ θα αποτελειτσαι απο το ενα state και το μονοπατι απο το starting state για να φτασει στο current_state
    visited_states = [] #στη σωρο εβαλα συνολο ενω εδω λιστα γιατι στο ερωτημα 5 χτυπαγε
    starting_state = problem.getStartState()
    root_from_starting_state = [] #καθε state(κομβος του δεντρου) θα εχει και μια λιστα απο τις κινησεις που εγιναν για να φταση εκει 
    
    queue.push((starting_state, root_from_starting_state)) #το μονοπατι απο το starting_state προς το starting_state ειναι προφανως η κενη λιστα

    while True:

        if queue.isEmpty():
            return []
        
        queue_elements = queue.pop()
        current_state = queue_elements[0]
        visited_states.append(current_state)
        root_to_current_state = queue_elements[1]

        if problem.isGoalState(current_state): 
            return root_to_current_state
        
        successors = problem.getSuccessors(current_state)
        if len(successors) != 0: #ελεγχω αν υπαρχουν current state successors
            for element in successors:
                next_state = element[0] #οριζω το next_state με το πρωτο στοιχειο της λιστας που γυρναει η getSuccessors
                if next_state not in visited_states: #ελεγχω αν η state εχει επισκευτη
                    if not queue.isEmpty():  #ελεγχω αν η next_state υπαρχει και στην ουρα αφου καθε φορα εισαγουμε στην ουρα ολους του γειτονες του καθε state
                                             #σε αντιθεση με τη σωρο    
                        list_of_first_queues_elements = [] #φτιαχνω κενη λιστα οπου θα αποθηκευω ολα τα states που ειναι στην ουρα 
                        counter = 0 #μετρητης ωστε να ξερω αν εχω διασχηση ολη την ουρα
                        for queues_elements in queue.list:
                            list_of_first_queues_elements += [ queues_elements[0] ]
                            if next_state != list_of_first_queues_elements[-1]: #ελεγχω μονο το τελευταιο εισαγωμεμο στοιχειο 
                                counter += 1
                            else:
                                break
                        if counter == len(queue.list): # ελεχω αν εχω διασχισει ολη την ουρα (next_state δεν ειναι ουτε στην ουρα ουτε εχει επισκευτει προηγουμενος)
                            root_to_next_state = root_to_current_state #το μονοπατι μεχρι να φτασουμε στο current state
                            root_to_next_state = root_to_next_state + [ element[1] ] # συν το επομενο βημα 
                            queue.push((next_state, root_to_next_state))
                    else:# αν η ουρα ειναι αδεια και next_state not in visited_states == True ειναι προφανες
                        root_to_next_state = root_to_current_state #το μονοπατι μεχρι να φτασουμε στο current state
                        root_to_next_state = root_to_next_state + [ element[1] ] # συν το επομενο βημα
                        queue.push((next_state, root_to_next_state))        

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""

    pqueue = util.PriorityQueue() #καθε στοιχειο του στακ θα αποτελειτσαι απο το ενα state και το μονοπατι απο το starting state για να φτασει στο current_state
    visited_states = set()
    starting_state = problem.getStartState()
    root_from_starting_state = [] #καθε state(κομβος του δεντρου) θα εχει και μια λιστα απο τις κινησεις που εγιναν για να φταση εκει 
    
    pqueue.push((starting_state, root_from_starting_state), 0)#η προτεραιοτητα καθοριζεται απο το κοστος του καθε state δλδ το κοστος της λιστας root_from_starting_state
    
    while True:

        if pqueue.isEmpty(): # μετα απο καθε προσθηκη κομβου αν εχει γινει στην ουρα προτεραιοτητας ελεγχω αν η λιστα ειναι αδεια 
            return []        #αν ειναι αδεια χωρις να εχω φτασει σε κατασταση στοχου δεν υπαρχει λυση και γυρναω κενη λιστα 
        
        pqueue_elements = pqueue.pop()
        current_state = pqueue_elements[0]
        visited_states.add(current_state)
        root_to_current_state = pqueue_elements[1]

        if problem.isGoalState(current_state): 
            return root_to_current_state

        successors = problem.getSuccessors(current_state)
        if len(successors) != 0: #ελεγχω αν υπαρχουν current state successors
            for element in successors:
                next_state = element[0] #οριζω το next_state με το πρωτο στοιχειο της λιστας που γυρναει η getSuccessors
                root_to_next_state = root_to_current_state + [ element[1] ] #το μονοπατι της επομενης καταστασης μεχρι να φτασουμε στο current state συν το επομενο βημα
                if next_state not in visited_states: #ελεγχω αν η state εχει επισκευτη
                    counter = 0 #μετρητης που ελεγχει αν εχει περαστει ολη η σωρος δλδ δεν υπαρχει το state στην ουρα προτεραιοτητας
                    for heaps_elements in pqueue.heap:
                        if next_state != heaps_elements[2][0]:#ελεγχω καθε state αν υπαρχει στη σωρο 
                            counter += 1
                        else:#αν φτασω εδω σημαινει οτι εχει βρεθει ιδιο state μεσα στην ουρα προτεραιοτητας
                            next_states_new_cost_of_actions = problem.getCostOfActions(root_to_next_state)#υπολογιζω το κοστος του καινουργιου μονοπατιου
                            next_states_old_cost_of_actions = problem.getCostOfActions(heaps_elements[2][1])#υπολογιζω κοστος παλιου μονοπατιου δλδ το μονοπατι που εχω διανυσει για να φτασω στο state που ειναι ηδη μεσα στην ουρα
                            if next_states_old_cost_of_actions > next_states_new_cost_of_actions:
                                pqueue.update((next_state, root_to_next_state), next_states_new_cost_of_actions)
                                break
                           
                    if counter == len(pqueue.heap):#αν φτασω εδω εχει διασχησθει ολη η ουρα προτεραιοτητας και δεν εχω βρει το next_state σε αυτη 
                        next_states_cost_of_actions = problem.getCostOfActions(root_to_next_state)
                        pqueue.push((next_state, root_to_next_state), next_states_cost_of_actions)#αρα το προσθετω αφου επισης δεν υπαρχει στο visited_states

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # σε αυτη τη συναρτηση δεν γραφω σχολια γιατι η λογικη ειναι η ιδια με τη ucs με τη διαφορα οτι η ucs ειναι uninformed αλγοριθμος αναζητησης με
    #συναρτηση αξιολογησης που λαμβανει υποψιν της μονο το κοστος για να φτασει στην επομενη κατασταση f(n) = g(n) ενω η a* search ειναι informed 
    #αλγοριθμος που λαμβανει αποφασεις βαση του κοστους για να φτασει στην επομενη κατασταση συν το κοστος μια χειριστικης συναρτησης που επιλεγουμε 
    #μεις πως θα ειναι υλοποιημενη και θα υπολογιζει το χειριστικο κοστος καθε καταστασης/κομβου f(n) = g(n) + h(n)
    pqueue = util.PriorityQueue() 
    visited_states = []
    starting_state = problem.getStartState()
    root_from_starting_state = [] 
    
    eval_func = problem.getCostOfActions(root_from_starting_state) + heuristic(starting_state, problem)
    pqueue.push((starting_state, root_from_starting_state), eval_func)

    while True:

        if pqueue.isEmpty():
            return []
        
        pqueue_elements = pqueue.pop()
        current_state = pqueue_elements[0]
        visited_states.append(current_state)
        root_to_current_state = pqueue_elements[1]

        if problem.isGoalState(current_state): 
            return root_to_current_state

        successors = problem.getSuccessors(current_state)
        if len(successors) != 0:
            for element in successors:
                next_state = element[0]
                root_to_next_state = root_to_current_state + [element[1]]
                if next_state not in visited_states:
                    counter = 0
                    for heaps_elements in pqueue.heap:
                        if next_state != heaps_elements[2][0]:
                            counter += 1
                        else:
                            next_states_new_eval_func = problem.getCostOfActions(root_to_next_state) + heuristic(next_state, problem)
                            next_states_old_eval_func = problem.getCostOfActions(heaps_elements[2][1]) + heuristic(next_state, problem)
                            if next_states_old_eval_func > next_states_new_eval_func:
                                pqueue.update((next_state, root_to_next_state), next_states_new_eval_func)
                                break
                            
                    if counter == len(pqueue.heap): 
                        next_states_eval_func = problem.getCostOfActions(root_to_next_state) + heuristic(next_state, problem)
                        pqueue.push((next_state, root_to_next_state), next_states_eval_func)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
