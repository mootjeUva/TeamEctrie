import random
from code.classes.traject import Traject
from code.classes.graph import Graph
from code.classes.verbinding import Connection
from typing import Dict, Any


def copy_dict(dictionary: Dict[Any, Any], avoid_value: str) -> Dict[Any, Any]:
    new_dict = {}
    dict_keys = dictionary.keys()
    for keys in dict_keys:
        if keys != avoid_value:
            new_dict[keys] = dictionary[keys]
    return new_dict


def random_algoritme2(graph: Graph, traject: Traject) -> None:

    # Select random starting station
    start_station = random.choice(list(graph.connections.keys()))
    distance = 0
    traject.add_station(start_station, distance)
    connections = graph.connections[start_station]
    tmp = start_station

    while True:
        ck_list = list(connections.keys())
        if len(ck_list) < 1:
            break
        next_station = random.choice(ck_list)
        distance = connections[next_station]
        if (traject.total_distance + distance) > 120:
            break
        con = Connection(tmp, next_station, distance)
        con2 = Connection(next_station, tmp, distance)
        traject.add_connection(con)
        traject.add_connection(con2)
        traject.add_station(next_station, distance)
        connections = graph.connections[next_station]
        connections = copy_dict(connections, tmp)
        tmp = next_station
