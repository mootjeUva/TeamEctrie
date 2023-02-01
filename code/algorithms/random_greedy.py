from code.classes.traject import Traject
from code.classes.lines import Lines
import random
import copy
from code.classes.graph import Graph


class Random_Greedy():
    """ Random_Greedy greedily creates trajects and add it to the line"""

    def __init__(self, graph: Graph, timeframe: int, max_traject: int) -> None: \
    
        self.graph = graph
        self.timeframe = timeframe
        self.max_trajects = max_traject

        # self.runtime = runtime
        self.best_K = 0
        self.line = Lines()

    def run(self) -> None:
        """ Run method which runs the random greedy algorithm for finding the best
        trajectory in the graph, given the time constraint of the traject. """

        # Create a new_graph by deepcopying self.graph
        new_graph = copy.deepcopy(self.graph)

        # Loop is executed max_trajects times to find the best possible trajectory's
        for i in range(self.max_trajects):

            # Create empty traject
            traject = Traject()

            # Define endpoint stations
            endpoint_stations = new_graph.endpoint_stations()

            # Select an unvisited starting (endpoint) station
            current_station = new_graph.not_visited_yet(endpoint_stations)
            
            # If no unvisited stations left, randomly choose a starting station
            if current_station is False:
                current_station = random.choice(
                    list(new_graph.stations.keys())
                    )

            # Set current station to is visited
            new_graph.stations[current_station].is_visited = True

            # While True keep adding stations to the traject
            while True:

                # Create station object of the station
                station_object = new_graph.stations[current_station]

                # Check if there is an unvisited connection
                if station_object.get_nearest_unvisited_connection() \
                   is not False:

                    # Find next station and distance, set connection's
                    # and station's is visited to true
                    next_station, con_object, distance = \
                        station_object.get_nearest_unvisited_connection()
                    distance = int(float(distance))
                    new_graph.stations[next_station].is_visited = True
                    con_object.is_visited = True

                    # Check if possible within timeframe
                    if (traject.total_distance + distance) > self.timeframe:
                        break

                    # Add station and connection to the traject
                    traject.add_station(next_station, distance)
                    traject.add_connection(con_object.connection_set)

                    # Change current station and keep track of tmp to avoid
                    # going back and forwards instantly between two stations
                    tmp = current_station
                    current_station = next_station

                else:
                    # Check if there is a highest potential connection 
                    # (except tmp)
                    if station_object.get_highest_potential_connection(
                            new_graph, tmp
                            ) is not False:
                        
                        # Get next station and distance
                        next_station, distance = \
                            station_object.get_highest_potential_connection(
                                new_graph, tmp
                                )
                        distance = int(float(distance))

                        # Check if possible within timeframe
                        if (traject.total_distance+distance) > self.timeframe:
                            break

                        # Add station to traject
                        # (connection not necessary because already visited)
                        traject.add_station(next_station, distance)

                        # Change current station
                        tmp = current_station
                        current_station = next_station
                    else:
                        break

            # There have to be at least 1 connection in a traject for being
            # a legit traject
            if len(traject.stations) <= 1:
                continue

            # Add found traject to line
            self.line.add_traject(traject)
