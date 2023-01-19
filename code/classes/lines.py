from .traject import Traject
from .graph import Graph
from .verbinding import Connection
from typing import List, Any


class Lines():

    def __init__(self) -> None:

        self.lines: List[Any] = []
        self.distances = 0
        self.connections: List[Connection] = []

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
        if p >= 1:
            p = 1
        T = len(self.lines)
<<<<<<< HEAD
        Min = sum(self.distances)
        p = self.compute_p()
=======
        Min = self.distances
>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602
        K = p*10000 - (T*100 + Min)

        return K
    
    def compute_p(self):
        total_stations = 0

        # Count how many stations in total are reached in self.lines
        for i in range(len(self.lines)):
            total_stations += len(self.lines[i])

        # connections / total connections
        p = round((total_stations - 1) / 28)

        return p
