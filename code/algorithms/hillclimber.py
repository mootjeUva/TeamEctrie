import copy
from code.algorithms.randomise import Randomise
from code.classes.graph import Graph
from code.classes.traject import Traject
from typing import Any, List


class HillClimber:
    """ The HillClimber class that changes a random node in the graph to
        a random valid value. Each improvement or equivalent solution is
        kept for the next iteration. """

    def __init__(self, graph: Graph, timeframe: int,
                 current_state: Any) -> None:
        self.graph = graph
        self.timeframe = timeframe
        self.current_state = current_state
        self.best_state = current_state
        self.scorelist: List[int] = []

    def run(self, iterations: int) -> None:
        """ This method takes one argument iterations and performs the 
            optimization process for the specified number of iterations. In 
            each iteration, it generates a random trajectory using the 
            generate_random_traject method, replaces the lowest-scoring 
            trajectory in the current state with the newly generated one. """
        
        for i in range(iterations):
            # Generate a new traject
            next_traject = self.generate_random_traject()
            # Make a copy of the current state
            current_state_copy = copy.deepcopy(self.current_state)
            # Remove lowest scoring traject
            self.remove_lowest_scoring_traject()
            # Add the generated traject to the line
            self.current_state.line.add_traject(next_traject)

            # If the new state has a higher score, update best state,
            # else set current state back to current_state copy
            if self.current_state.line.score(self.graph) > \
               self.best_state.line.score(self.graph):
                self.best_state = current_state_copy
            else:
                self.current_state = current_state_copy
            self.scorelist.append(self.best_state.line.score(self.graph))

    def generate_random_traject(self) -> Traject:
        """ This method generates a single random trajectory using the Randomise class. """

        # Generate a single random traject
        random_traject = Randomise(self.graph, self.timeframe, 1)
        random_traject.run()
        return random_traject.line.trajects[0]

    def remove_lowest_scoring_traject(self) -> None:
        """ This method removes the lowest-scoring trajectory from the current 
            state. """
        
        # Create an empty list
        score = []

        # Remove every traject one at a time and calculate the score
        for traject in self.current_state.line.trajects.copy():
            self.current_state.line.remove_traject(traject)
            score.append(self.current_state.line.score(self.graph))
            self.current_state.line.add_traject(traject)

        # Remove the lowest scoring traject
        lowest_score_index = score.index(max(score))
        self.current_state.line.remove_traject(
            self.current_state.line.trajects[lowest_score_index]
            )
