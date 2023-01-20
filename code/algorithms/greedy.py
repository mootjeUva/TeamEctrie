from copy import deepcopy
from code.classes.station import Station
from code.classes.graph import Graph
from code.classes.traject import Traject


class Greedy():

    def __init__(self, graph: Graph, traject: Traject) -> None:

        self.graph = deepcopy(graph)
        self.traject = traject

    def get_next_station(self, stations: Station) -> None:
        pass
