from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.verbinding import Connection
from code.classes.lines import Lines
import time
import random
import copy

class Greedy2():
    """
    2nd version of the greedy algorithm which look for unvisited connections instead of stations
    """
    def __init__(self, graph, timeframe, max_traject, runtime):
        self.graph = graph
        self.timeframe = timeframe
        self.max_trajects = max_traject
        self.runtime = runtime
        self.best_K = 0
        self.best_line = Lines()



    def run(self):
        """
        run method
        """
        start = time.time()
        n_runs = 0

        while time.time() - start < self.runtime:
            n_runs += 1
            print(f"run: {n_runs}")

            # for each try, create a new graph and new line
            new_graph = copy.deepcopy(self.graph)
            line = Lines()

            for i in range(self.max_trajects):
                
                # Create empty traject
                traject = Traject()

                # Define endpoint stations
                endpoint_stations = self.graph.endpoint_stations()

                # Select an unvisited starting station
                current_station = self.graph.not_visited_yet(endpoint_stations)

                if current_station is False:
                    current_station = random.choice(self.graph.stations.keys())

                while True:
                    station_object = self.graph.stations[current_station]
                    # Check if there is an unvisited station
                    if station_object.get_nearest_unvisited_connection(self.graph) is not False:

                        # Find next station and distance, set connections is visited to true
                        next_station, con_object, distance = station_object.get_nearest_unvisited_connection(self.graph)
                        distance = int(float(distance))
                        con_object.is_visited = True
                        new_graph.stations[next_station].is_visited = True

                        # Check if possible within timeframe
                        if (traject.total_distance + distance) > self.timeframe:
                            break

                        # Add station and connection to the traject
                        traject.add_station(next_station, distance)
                        traject.add_connection(con_object.connection_set)

                        # Change current station
                        current_station = next_station

                    else:
                        pass








                    


                

