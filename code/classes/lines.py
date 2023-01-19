from .traject import Traject
from .graph import Graph


class Lines():

    def __init__(self) -> None:

        self.lines = []
        self.distances = 0
        self.connections = []

    def add_traject(self, traject: Traject) -> None:

        train_list = list(traject.stations.keys())

        if train_list not in self.lines:
            self.lines.append(train_list)
            self.distances += traject.total_distance
        for con in traject.ridden_connections:
            if con not in self.connections:
                self.connections.append(con)

        self.connections = list(dict.fromkeys(self.connections))

    def score(self, graph: Graph) -> float:

        p = float(len(self.connections)/len(graph.all_connections))
        T = len(self.lines)
        Min = self.distances
        K = p*10000 - (T*100 + Min)

        return K
