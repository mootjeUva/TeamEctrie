import copy
from code.algorithms.greedy import RandomGreedy
from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.verbinding import Connection
from code.classes.lines import Lines
import random
from code.algorithms.randomise import Randomise

class HillClimber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """

    def __init__(self, graph, timeframe, max_trajects):
        self.graph = graph
        self.timeframe = timeframe
        self.max_trajects = max_trajects
        self.current_state = RandomGreedy(self.graph, self.timeframe, self.max_trajects)
        self.best_state = self.current_state
    
    def run(self,iterations):
        for i in range(iterations):
            next_traject = self.generate_random_traject()
            current_state_copy = copy.deepcopy(self.current_state)
            self.remove_lowest_scoring_traject()
            self.current_state.line.add_traject(next_traject.line)

            if self.current_state.line.score(self.graph) > self.best_state.line.score(self.graph):
                self.best_state = self.current_state
            else:
                self.current_state = current_state_copy
        
    
    def generate_random_traject(self):
        
        # Generate a single random traject
        random_traject = Randomise(self.graph, self.timeframe, 1)
        return random_traject
    
    def remove_lowest_scoring_traject(self):
        # create an empty list
        score = []
        # remove every traject one at a time and calculate the score
        for traject in self.current_state.line.lines.copy():
            self.current_state.line.lines.remove(traject)
            score.append(self.current_state.line.score(self.graph))
            self.current_state.line.lines.append(traject)
        
        # remove the lowest scoring traject
        lowest_score_index = score.index(min(score))
        self.current_state.line.lines.remove(self.current_state.line.lines[lowest_score_index])



