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


def random_algorithm(graph: Graph, traject: Traject) -> None:

    # Select random starting station
    start_station = random.choice(list(graph.connections.keys()))

    # Set starting distance equal to 0
    distance = 0

    # Add starting station to traject and save the connections
    traject.add_station(start_station, distance)
    connections = graph.connections[start_station]
    tmp = start_station

    while True:

        # Find connection key list
        ck_list = list(connections.keys())

        # Check if endpoint reached
        if len(ck_list) < 1:
            break

        # Pick a random station and find the distance to it
        next_station = random.choice(ck_list)
        distance = connections[next_station]

        # Check if the next station can be reached within the timeframe
        if (traject.total_distance + distance) > 120:
            break

        # Add connections and station to the trajrect
        con_object = Connection(tmp, next_station, distance)
        con_stations = [con_object.station1, con_object.station2]
        # con2 = Connection(next_station, tmp, distance)
        traject.add_connection(con_stations)
        # traject.add_connection(con2)
        traject.add_station(next_station, distance)
        connections = graph.connections[next_station]
        connections = copy_dict(connections, tmp)
        tmp = next_station
