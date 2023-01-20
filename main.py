from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.lines import Lines
from code.algorithms.randomise import random_algorithm
import numpy as np


if __name__ == "__main__":

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
                random_algorithm(graph, traject)
                line.add_traject(traject)
        score = line.score(graph)
        score_list.append(score)

    average_score = round(sum(score_list)/len(score_list))
    minn = sorted(score_list, reverse=False)[0]
    maxx = sorted(score_list, reverse=True)[0]
    standard_deviation = round(np.std(score_list))
    print(f"Average score = {average_score}")
    print(f"Standard deviation = {standard_deviation}")
    print(f"(Min, Max) = ({minn}, {maxx})")
