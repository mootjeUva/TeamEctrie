from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.verbinding import Connection
from code.classes.lines import Lines
import random


class RandomGreedy():

    def __init__(self, graph: Graph, timeframe: int, max_traject: int) -> None:

        self.graph = graph
        self.timeframe = timeframe
        self.max_trajects = max_traject
        self.line = Lines()

    def run(self) -> None:
        """ Greedily chooses station which has shortest distance, and is
            unvisited. In case no unvisited connections, algorithm chooses
            connection with highest potential, which implies that this visited
            connection has unvisited connections by itself. """

        for i in range(self.max_trajects):

            traject = Traject()

            # Define endpoint stations
            endpoint_stations = self.graph.endpoint_stations()

            # Select an unvisited starting station
            current_station = self.graph.not_visited_yet(endpoint_stations)

            if current_station is False:
                return

            # Add starting station to traject
            traject.add_station(current_station, 0)

            # Set visited to true
            self.graph.stations[current_station].is_visited = True

            while True:
                # Find the station as an object
                station_object = self.graph.stations[current_station]

                # Check if there is an unvisited station
                if station_object.get_nearest_unvisited_station(
                                                                self.graph
                                                                ) is not False:

                    # Find next station and distance
                    next_station, distance = station_object.get_nearest_unvisited_station(self.graph)
                    distance = int(float(distance))
                    # Check if possible within timeframe
                    if (traject.total_distance + distance) > self.timeframe:
                        break

                    # Set is visited to true
                    self.graph.stations[next_station].is_visited = True

                    # Add id to the traject
                    traject.add_station(next_station, distance)

                    # Add connections and station to the traject
                    con_object = Connection(current_station,
                                            next_station, distance)
                    traject.add_connection(con_object.connection_set)

                    # Change current station
                    current_station = next_station

                else:
                    # Next station is highest potential station
                    next_station = station_object.highest_potential(self.graph)

                    # If no hightest potential connection, break
                    if next_station is False:
                        next_station = random.choice(list(self.graph.connections[current_station].keys()))

                    # Find distance to this station
                    distance = self.graph.distance_between_stations(
                                                    current_station,
                                                    next_station)
                    distance = int(float(distance))
                    # Check if possible within timeframe
                    if (traject.total_distance + distance) > self.timeframe:
                        break

                    # Add id to the traject
                    traject.add_station(next_station, distance)

                    # Add connections and station to the traject
                    con_object = Connection(current_station,
                                            next_station, distance)
                    traject.add_connection(con_object.connection_set)

                    # Change current station
                    current_station = next_station

                if len(traject.stations) <= 1:
                    continue

            self.line.add_traject(traject)
