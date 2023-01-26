import copy
from code.algorithms.greedy import RandomGreedy
from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.lines import Lines
from typing import Any


class HillClimber():
    """ The HillClimber class that changes a random node in the graph to a
        random valid value. Each improvement or equivalent solution is kept
        for the next iteration. """

    def __init__(self, graph: Graph, best_line: Lines, timeframe: int) -> None:

        self.graph = graph
        self.new_graph = copy.deepcopy(graph)
        self.timeframe = timeframe
        self.best_line = best_line
        self.old_score = best_line.score(self.graph)

    def remove_lowest_scoring_traject(self) -> Traject:

        for i in range(len(self.best_line.lines)):
            K_list = []
            K_list.append(self.K_traject(self.best_line.lines[i]))

        minn_index = K_list.index(min(K_list))
        lowest_scoring_traject = K_list.pop(minn_index)
        return lowest_scoring_traject

    def create_randomgreedy_traject(self) -> Traject:

        traject = Traject()
        for s in range(len(RandomGreedy(self.new_graph, self.timeframe, 1))):
            pass

        return traject

    def compare_s(self, traject_old: Traject, traject_new: Traject) -> bool:

        if self.K_traject(traject_new) > self.K_traject(traject_old):
            return True
        return False

    def K_traject(self, traject: Traject) -> Any:
        """" Calculate K for one traject with T = 1. """

        p = len(traject.ridden_connections) / len(self.graph.all_connections)
        K = p * 1000 - traject.total_distance

        return K

    def run(self) -> Lines:
        """ Run method of hillclimber. """

        removed_traject = self.remove_lowest_scoring_traject()
        new_traject = self.create_randomgreedy_traject()

        if self.compare_s(removed_traject, new_traject) is True:
            self.best_line.add_traject(new_traject)
            self.graph = self.new_graph
        else:
            self.best_line.add_traject(removed_traject)

        return self.best_line
