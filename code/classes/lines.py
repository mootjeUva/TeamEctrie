from .traject import Traject
from .graph import Graph
from .verbinding import Connection
from typing import List, Any


class Lines():

    def __init__(self) -> None:

        self.lines: List[Any] = []
        self.distances = 0
        self.connections: List[set[str, str]] = []

    def add_traject(self, traject: Traject) -> None:

        train_list = traject.stations

        if train_list not in self.lines:
            self.lines.append(train_list)
            self.distances += traject.total_distance
        
        # Append all new connection sets to self.conections
        for con_set in traject.ridden_connections:
            if con_set not in self.connections:
                self.connections.append(con_set)

    def score(self, graph: Graph) -> float:

        p = float(len(self.connections)/(len(graph.all_connections)))
        if p >= 1:
            p = 1
        T = len(self.lines)
        Min = self.distances
        K = p*10000 - (T*100 + Min)
        
        return K
