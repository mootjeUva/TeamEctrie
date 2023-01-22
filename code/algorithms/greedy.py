from copy import deepcopy
from code.classes.station import Station
from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.verbinding import Connection
import random

class RandomGreedy():

    def __init__(self, graph: Graph, traject: Traject, timeframe: int) -> None:

        self.graph = graph
        self.traject = traject
        self.timeframe = timeframe

    def run(self):
        """
        Greedily chooses station which has shortest distance, and is unvisited
        """
        # Select an unvisited starting station
        current_station = self.graph.not_visited_yet()

        if current_station == False:
            return

        # Add starting station to traject
        self.traject.add_station(current_station, 0)

        # Set visited to true
        self.graph.stations[current_station].is_visited = True

        while True:
            # Find the station as an object
            station_object = self.graph.stations[current_station]

            # Check if there is an unvisited connection
            if station_object.get_nearest_unvisited_connection(self.graph) != False:

                # Find next station and distance
                next_station, distance = station_object.get_nearest_unvisited_connection(self.graph)

                # Check if possible within timeframe
                if (self.traject.total_distance + distance) > self.timeframe:
                    break

                # Set is visited to true
                self.graph.stations[next_station].is_visited = True

                # Add id to the traject
                self.traject.add_station(next_station, distance)

                # Add connections and station to the traject
                con_object = Connection(current_station, next_station, distance)
                self.traject.add_connection(con_object.connection_set)

                # Change current station
                current_station = next_station

            else:
                # Next station is highest potential station
                next_station = station_object.highest_potential(self.graph)

                # If no hightest potential connection, break
                if next_station == False:
                    next_station = random.choice(list(self.graph.connections[current_station].keys()))

                # Find distance to this station
                distance = self.graph.distance_between_stations(current_station, next_station)

                # Check if possible within timeframe
                if (self.traject.total_distance + distance) > self.timeframe:
                    break

                # Add id to the traject
                self.traject.add_station(next_station, distance)

                # Add connections and station to the traject
                con_object = Connection(current_station, next_station, distance)
                self.traject.add_connection(con_object.connection_set)

                # Change current station
                current_station = next_station









                # # Randomly choose next station and find it's distance
                # next_station = random.choice(list(self.graph.connections[current_station].keys()))
                # distance = self.graph.connections[current_station][next_station]

                # # Check if possible within timeframe
                # if (self.traject.total_distance + distance) > 120:
                #     break

                # # Add it to the traject
                # self.traject.add_station(next_station, distance)

                # # Add connections and station to the trajrect
                # con_object = Connection(current_station, next_station, distance)
                # self.traject.add_connection(con_object.connection_set)

                # # Change current station
                # current_station = next_station
                



