from .traject import Traject
from .graph import Graph
from typing import List, Any, Set


class Lines():
    """ The Lines class is used to keep track of all the routes taken
        by multiple trajects. """

    def __init__(self) -> None:
        """ Initialize the Lines class."""

        self.lines: List[Any] = []
        self.distances = 0
        self.connections: List[Set[str]] = []
        self.trajects: List[Traject] = []

    def add_traject(self, traject: Traject) -> None:
        """ Add a Traject instance to self.trajects. """

        self.trajects.append(traject)
        train_list = traject.stations

        # Add new train route list to self.lines
        if train_list not in self.lines:
            self.lines.append(train_list)
            self.distances += traject.total_distance

        # Append all new connection sets to self.conections
        for con_set in traject.ridden_connections:
            if con_set not in self.connections:
                self.connections.append(con_set)

    def remove_traject(self, traject: Traject) -> None:
        """ Remove a Traject instance from self.trajects. """

        if traject in self.trajects:
            self.trajects.remove(traject)
            train_list = traject.stations

        # Remove train route list from self.lines
        if train_list in self.lines:
            self.lines.remove(train_list)
            self.distances -= traject.total_distance

        # Remove all new connection sets to self.connection
        for con_set in traject.ridden_connections:
            if con_set in self.connections:
                self.connections.remove(con_set)

    def score(self, graph: Graph) -> float:
        """ Calculate and return the score based on the given graph. """

        # Total number of unique train routes
        T = len(self.lines)
        # Proportion of all connections used
        p = float((len(self.connections))/(len(graph.all_connections)))
        # Total distance traveled
        Min = self.distances
        # Calculate the score using the formula given
        K = p*10000 - (T*100 + Min)

        return K
