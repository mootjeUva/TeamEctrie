import random
from graph import Graph
from traject import Traject

def not_visited_yet(graph, connections):
    """
    This method returns a station from connections list if it is not visited yet, 
    if all stations in connections are visited function returns False
    """
    for station in connections:
        if graph.stations[station].is_visited == False:
            return station
    return False

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
    # Determine connections of first station
    current_station_connections = graph.connections[current_station] 

    # Infinite loop to add randomly stations to traject
    while True:
        # Choose next station which is not visited yet
        next_station = not_visited_yet(graph ,current_station_connections)
        # Check if next_station is visited or not
        if next_station != False:
            # Compute distance to next_station
            distance = current_station_connections[next_station]
            # Check if possible within timeframe
            if traject.check_timeframe(distance) == False:
                break
            # Set station's is_visited to true, add it to the traject, change current_station and determine it's connections
            graph.stations[next_station].is_visited = True
            traject.add_station(next_station, distance)
            current_station = next_station
            current_station_connections = graph.connections[current_station]
        else:
            break
    return traject

def random_algorithm(graph):
    """
    This method creates at most 7 trajects and returns the score of the goalfunction
    """
    traject_dict = {}
    i = 1

    # Randomly create a traject and add it to the traject_dict
    while len(traject_dict.keys()) < 7:
        traject = Traject()
        traject = random_traject(graph)
        if len(traject.stations) == 1:
            break
        traject_dict[f'traject{i}'] = [len(traject.stations), traject.total_distance]
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

def main():
    graph = Graph('../data/StationsHolland.csv', '../data/ConnectiesHolland.csv')
    random_algorithm(graph)

if __name__ == "__main__":
    main()