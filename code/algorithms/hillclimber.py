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

        for i in range(iterations):
            next_traject = self.generate_random_traject()
            current_state_copy = copy.deepcopy(self.current_state)
            self.remove_lowest_scoring_traject()
            self.current_state.line.add_traject(next_traject)

            if self.current_state.line.score(self.graph) > \
               self.best_state.line.score(self.graph):
                self.best_state = current_state_copy
            else:
                self.current_state = current_state_copy
            self.scorelist.append(self.best_state.line.score(self.graph))

    def generate_random_traject(self) -> Traject:

        # Generate a single random traject
        random_traject = Randomise(self.graph, self.timeframe, 1)
        random_traject.run()
        return random_traject.line.trajects[0]

    def remove_lowest_scoring_traject(self) -> None:

        # create an empty list
        score = []
        # remove every traject one at a time and calculate the score
        for traject in self.current_state.line.trajects.copy():
            self.current_state.line.remove_traject(traject)
            score.append(self.current_state.line.score(self.graph))
            self.current_state.line.add_traject(traject)

        # remove the lowest scoring traject
        lowest_score_index = score.index(max(score))
        self.current_state.line.remove_traject(
            self.current_state.line.trajects[lowest_score_index]
            )
