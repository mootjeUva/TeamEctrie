import random
import copy 
from traject import Traject

def random_algorithm(graph, traject):
    
    # Select random starting station
    start_station = random.choice(list(graph.connections.keys()))
    traject.add_station(start_station, 0)
    connections = graph.connections[start_station]
    
    while True:
        next_station = random.choice(list(connections.keys()))
        distance = connections[next_station]
        traject.add_station(next_station, distance)
        connections = graph.connections[next_station]





    
    






    


    