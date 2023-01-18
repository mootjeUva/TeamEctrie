from copy import deepcopy
from classes.station import Station
from classes.graph import Graph
from classes.traject import Traject


class Greedy():

    def __init__(self, graph: Graph, traject: Traject) -> None:

        self.graph = deepcopy(graph)
        self.traject = traject

    def get_next_station(self, stations: Station) -> str:
        pass
