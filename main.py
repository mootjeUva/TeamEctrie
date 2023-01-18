from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.station import Station
from code.classes.verbinding import Connection
from code.algorithms import randomise, greedy


if __name__ == "__main__":

    graph = Graph('data/StationsHolland.csv',
                  'data/ConnectiesHolland.csv')

    outputlist = []
    for i in range(10):
        traject = Traject()
        randomise.random_algorithm(graph, traject)
        train_list = list(traject.stations.keys())
        if train_list not in outputlist:
            outputlist.append(train_list)

    print(outputlist)
