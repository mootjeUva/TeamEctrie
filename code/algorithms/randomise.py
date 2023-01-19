import random
<<<<<<< HEAD
from code.classes.traject import Traject
from code.classes.graph import Graph
from code.classes.lines import Lines
=======
from code.classes.graph import Graph
from code.classes.traject import Traject


def not_visited_yet(graph: Graph, connections):
    """ This method returns a station from connections list if it is not
        visited yet, if all stations in connections are visited function
        returns False. """

    for station in connections:
        if graph.stations[station].is_visited is False:
            return station
    return False
>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602


def random_traject(graph: Graph) -> Traject:
    """ This method returns a random traject of at most 120 minutes. """

    # Create empty traject
    traject = Traject()

    # Randomly choose a station to start from and add to traject
    current_station = random.choice(list(graph.connections.keys()))
    traject.add_station(current_station, 0)

    # Set first station's is visited to true
    graph.stations[current_station].is_visited = True
<<<<<<< HEAD
=======

    # Determine connections of first station
    current_station_connections = graph.connections[current_station]
>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602

    while True:
        # Choose next station which is not visited yet
<<<<<<< HEAD
        next_station = graph.not_visited_yet(current_station)
=======
        next_station = not_visited_yet(graph, current_station_connections)

>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602
        # Check if next_station is visited or not
        if next_station is not False:
            # Compute distance to next_station
<<<<<<< HEAD
            distance = graph.distance_between_stations(current_station, next_station)
=======
            distance = current_station_connections[next_station]

>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602
            # Check if possible within timeframe
            if traject.check_timeframe(distance) is False:
                break

            # Set station's is_visited to true, add it to the traject, change
            # current_station and determine it's connections
            graph.stations[next_station].is_visited = True
            traject.add_station(next_station, distance)
            current_station = next_station
        else:
            break
    return traject

<<<<<<< HEAD
def random_algorithm(graph):
    """
    This method creates at most 7 trajects and returns the score of the goalfunction
    """
    lines = Lines()
=======

def random_algorithm(graph: Graph) -> float:
    """ This method creates at most 7 trajects,
        and returns the score of the goalfunction. """

    traject_dict = {}
    i = 1
>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602

    # Randomly create (at most 7) trajects till length of the traject can't be greater than 1
    for i in range(7):
        traject = Traject()
        traject = random_traject(graph)
        if len(traject.stations) == 1:
            break
<<<<<<< HEAD
        lines.add_traject(traject)
    
    return lines
=======
        traject_dict[f'traject{i}'] = [len(traject.stations),
                                       traject.total_distance]
        i += 1

    # Compute total stations
    total_stations = 0
    for traject in traject_dict:
        total_stations += traject_dict[traject][0]

    # Compute total traject
    total_traject = len(traject_dict.keys())

    # Compute total minute
    total_minute = 0
    for traject in traject_dict:
        total_minute += traject_dict[traject][1]

    # Compute score and return it
    p = total_stations / 22
    T = total_traject
    Min = total_minute
    K = p*10000 - (T*100 + Min)

    print(K)
    return K
>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602
