from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.station import Station
from code.classes.verbinding import Connection
from code.classes.lines import Lines
from code.algorithms import randomise, greedy
from code.algorithms.randomise2 import random_algoritme2


if __name__ == "__main__":

    line = Lines()
    graph = Graph('data/StationsHolland.csv',
                  'data/ConnectiesHolland.csv')
    j = 0
    for i in range(7):
        if len(line.connections) >= len(graph.all_connections) or len(line.lines) >= 7:
            break
        else:
            traject = Traject()
            random_algoritme2(graph, traject)
            line.add_traject(traject)

    score = line.score(graph)
    print(score)
