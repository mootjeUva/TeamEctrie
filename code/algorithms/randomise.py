import random
from code.classes.traject import Traject
from code.classes.verbinding import Connection
from code.classes.lines import Lines
from code.classes.graph import Graph
from typing import Dict, Any


class Randomise():
    """ Randomise randomly creates trajects, in other words; it randomly
        assigns a begin station, then it randomly chooces connections
        except from the last visited station. """

    def __init__(self, graph: Graph, timeframe: int, max_traject: int) -> None:

        self.graph = graph
        self.timeframe = timeframe
        self.max_trajects = max_traject
        self.line = Lines()

    def copy_dict(self, dictionary: Dict[Any, Any],
                  avoid_value: str) -> Dict[Any, Any]:
        """ This method returns a dict of connections without the
            connection to be avoided (last visited station). """

        new_dict = {}
        dict_keys = dictionary.keys()

        for keys in dict_keys:
            if keys != avoid_value:
                new_dict[keys] = dictionary[keys]

        return new_dict

    def run(self) -> None:
        """ Run method which runs the algorithm. """

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
                distance = int(float(connections[next_station]))

                # Check if the next station can be reached within the timeframe
                if (traject.total_distance + distance) > self.timeframe:
                    break

                # Add connections and station to the trajrect
                con_object = Connection(tmp, next_station, distance)
                traject.add_connection(con_object.connection_set)

                # Add next_station to traject, find connections
                # and set temporary variable to next_station
                traject.add_station(next_station, distance)
                connections = self.graph.connections[next_station]
                connections = self.copy_dict(connections, tmp)
                tmp = next_station

                # There has to be at least 1 connection to be a legit traject
                if len(traject.stations) <= 1:
                    continue

            # Add traject to line
            self.line.add_traject(traject)
