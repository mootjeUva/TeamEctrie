import random
from code.classes.traject import Traject
from code.classes.graph import Graph
from code.classes.lines import Lines

def random_traject(graph):
    """
    This method returns a random traject of at most 120 minutes
    """
    # Create empty traject
    traject = Traject()
    # Randomly choose a station to start from and add to traject
    current_station = random.choice(list(graph.connections.keys()))
    traject.add_station(current_station, 0)
    # Set first station's is visited to true
    graph.stations[current_station].is_visited = True

    while True:
        # Choose next station which is not visited yet
        next_station = graph.not_visited_yet(current_station)
        # Check if next_station is visited or not
        if next_station != False:
            # Compute distance to next_station
            distance = graph.distance_between_stations(current_station, next_station)
            # Check if possible within timeframe
            if traject.check_timeframe(distance) == False:
                break
            # Set station's is_visited to true, add it to the traject, change current_station and determine it's connections
            graph.stations[next_station].is_visited = True
            traject.add_station(next_station, distance)
            current_station = next_station
        else:
            break
    return traject

def random_algorithm(graph):
    """
    This method creates at most 7 trajects and returns the score of the goalfunction
    """
    lines = Lines()

    # Randomly create (at most 7) trajects till length of the traject can't be greater than 1
    for i in range(7):
        traject = Traject()
        traject = random_traject(graph)
        if len(traject.stations) == 1:
            break
        lines.add_traject(traject)
    
    return lines