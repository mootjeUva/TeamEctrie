import random
from classes.traject import Traject
from classes.graph import Graph


def random_algorithm(graph: Graph, traject: Traject) -> None:

    # Select random starting station
    start_station = random.choice(list(graph.connections.keys()))
    traject.add_station(start_station, 0)
    connections = graph.connections[start_station]

    while True:
        next_station = random.choice(list(connections.keys()))
        distance = connections[next_station]
        traject.add_station(next_station, distance)
        connections = graph.connections[next_station]
