from code.classes.traject import Traject
from code.classes.lines import Lines
import random
import copy
from code.classes.graph import Graph


class Greedy2():
    """ 2nd version of the greedy algorithm which look for unvisited
        connections instead of stations. """

    def __init__(self, graph: Graph, timeframe: int, max_traject: int) -> None:

        self.graph = graph
        self.timeframe = timeframe
        self.max_trajects = max_traject

        # self.runtime = runtime
        self.best_K = 0
        self.line = Lines()

    def run(self) -> None:
        """ run method. """

        # start = time.time()
        # n_runs = 0

        # while time.time() - start < self.runtime:
        #     n_runs += 1
        #     print(f"run: {n_runs}")

        # for each try, create a new graph and new line
        new_graph = copy.deepcopy(self.graph)

        for i in range(self.max_trajects):

            # Create empty traject
            traject = Traject()

            # Define endpoint stations
            endpoint_stations = new_graph.endpoint_stations()

            # Select an unvisited starting station
            current_station = new_graph.not_visited_yet(endpoint_stations)

            if current_station is False:
                current_station = random.choice(
                    list(new_graph.stations.keys())
                    )

            new_graph.stations[current_station].is_visited = True

            while True:
                station_object = new_graph.stations[current_station]

                # Check if there is an unvisited station
                if station_object.get_nearest_unvisited_connection() \
                   is not False:

                    # Find next station and distance, set connections
                    # is visited to true
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

                    # Change current station
                    tmp = current_station
                    current_station = next_station

                else:
                    # Go to next station with highest potential (if not tmp)
                    if station_object.get_highest_potential_connection(
                            new_graph, tmp
                            ) is not False:
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

                # len(traject.stations) can be adjusted to alpha to
                # determine its optimal parameter
                if len(traject.stations) <= 3:
                    continue

            self.line.add_traject(traject)
