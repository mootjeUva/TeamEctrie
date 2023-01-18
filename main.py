from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.station import Station
from code.classes.lines import Lines
from code.classes.verbinding import Connection
from code.algorithms import randomise, greedy


if __name__ == "__main__":

    lineslist = []
    scoreslist = []

    for i in range(1):
        graph = Graph('data/StationsHolland.csv',
                  'data/ConnectiesHolland.csv')
        lines = randomise.random_algorithm(graph)
        lineslist.append(lines.lines)
        scoreslist.append(lines.score())
    
    print(lines.lines)
    print(lines.score())