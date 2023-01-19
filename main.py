from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.station import Station
from code.classes.lines import Lines
from code.classes.verbinding import Connection
from code.classes.lines import Lines
from code.algorithms import randomise, greedy
from code.algorithms.randomise2 import random_algoritme2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    lineslist = []
    scoreslist = []

    for i in range(1):
        graph = Graph('data/StationsHolland.csv',
                  'data/ConnectiesHolland.csv')

    score_list = []
    for j in range(100000):
        line = Lines()
        for i in range(7):
            if len(line.lines) >= 7 or \
                   len(line.connections) >= len(graph.all_connections):
                break
            else:
                traject = Traject()
                random_algoritme2(graph, traject)
                line.add_traject(traject)
        score = line.score(graph)
        score_list.append(score)

    average_score = round(sum(score_list)/len(score_list))
    standard_deviation = round(np.std(score_list))
    print(f"Average score = {average_score}")
    print(f"Standard deviation = {standard_deviation}")