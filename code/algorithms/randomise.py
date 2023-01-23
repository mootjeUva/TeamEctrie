import random
from code.classes.traject import Traject
from code.classes.graph import Graph
from code.classes.verbinding import Connection
from code.classes.lines import Lines
from typing import Dict, Any

class Randomise():
    
    def __init__(self, graph, timeframe, max_trajects):
        self.graph = graph
        self.timeframe = timeframe
        self.max_trajects = max_trajects
        self.line = Lines()


    def copy_dict(self, dictionary: Dict[Any, Any], avoid_value: str) -> Dict[Any, Any]:
        new_dict = {}
        dict_keys = dictionary.keys()
        for keys in dict_keys:
            if keys != avoid_value:
                new_dict[keys] = dictionary[keys]
        return new_dict


    def run(self) -> None:

        for i in range(self.max_trajects):
            # Create empty traject
            traject = Traject()

            # Select random starting station
            start_station = random.choice(list(self.graph.connections.keys()))

            # Set starting distance equal to 0
            distance = 0

            # Add starting station to traject and save the connections
            traject.add_station(start_station, distance)
            connections = self.graph.connections[start_station]
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
                if (traject.total_distance + distance) > self.timeframe:
                    break

                # Add connections and station to the trajrect
                con_object = Connection(tmp, next_station, distance)
                traject.add_connection(con_object.connection_set)

                # Add next_station to traject, find connections end set temporary variable to next_station
                traject.add_station(next_station, distance)
                connections = self.graph.connections[next_station]
                connections = self.copy_dict(connections, tmp)
                tmp = next_station

                if len(traject.stations) <= 1:
                    continue

            self.line.add_traject(traject)
