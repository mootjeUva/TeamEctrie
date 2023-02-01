from .traject import Traject
from .graph import Graph
from typing import List, Any, Set


class Lines():

    def __init__(self) -> None:

        self.lines: List[Any] = []
        self.distances = 0
        self.connections: List[Set[str]] = []
        self.trajects: List[Traject] = []

    def add_traject(self, traject: Traject) -> None:
        self.trajects.append(traject)

        train_list = traject.stations

        if train_list not in self.lines:
            self.lines.append(train_list)
            self.distances += traject.total_distance

        # Append all new connection sets to self.conections
        for con_set in traject.ridden_connections:
            if con_set not in self.connections:
                self.connections.append(con_set)

    def remove_traject(self, traject: Traject) -> None:
        if traject in self.trajects:
            self.trajects.remove(traject)
            train_list = traject.stations

        if train_list in self.lines:
            self.lines.remove(train_list)
            self.distances -= traject.total_distance

        # Remove all new connection sets to self.connection
        for con_set in traject.ridden_connections:
            if con_set in self.connections:
                self.connections.remove(con_set)

    def score(self, graph: Graph) -> float:

        T = len(self.lines)
        p = float((len(self.connections))/(len(graph.all_connections)))
        Min = self.distances
        K = p*10000 - (T*100 + Min)

        return K
