from code.classes.graph import Graph
from code.classes.traject import Traject
from code.classes.lines import Lines
from code.algorithms.randomise import random_algorithm
import numpy as np
from code.algorithms.greedy import RandomGreedy


if __name__ == "__main__":

    # Create graph and empty traject
    graph = Graph('data/StationsHolland.csv',
                  'data/ConnectiesHolland.csv')

    #-------------------------Random Algorithm-------------------------
    random_score_list = []
    for j in range(10000):
        line = Lines()
        for i in range(7):
            if len(line.lines) >= 7 or \
                   len(line.connections) >= len(graph.all_connections):
                break
            else:
                traject = Traject()
                random_algorithm(graph, traject)
                line.add_traject(traject)
        random_score_list.append(line.score(graph))

    random_average_score = round(sum(random_score_list)/len(random_score_list))
    random_minn = sorted(random_score_list, reverse=False)[0]
    random_maxx = sorted(random_score_list, reverse=True)[0]
    random_standard_deviation = round(np.std(random_score_list))
    print(f"Random average_score = {random_average_score}")
    print(f"Random standard_deviation = {random_standard_deviation}")
    print(f"Random (Min, Max) = ({random_minn}, {random_maxx})")

    #---------------------------RandomGreedy Algorithm---------------------------
    greedy_score_list = []
    
    for i in range(10000):
        graph = Graph('data/StationsHolland.csv',
                  'data/ConnectiesHolland.csv')
        line = Lines()
        for j in range(7):
            if len(line.lines) >= 7 or \
                   len(line.connections) >= len(graph.all_connections):
                break
            traject = Traject()
            gr = RandomGreedy(graph, traject)
            gr.run()
            if len(traject.stations.keys()) <= 1:
                continue
            line.add_traject(traject)
        greedy_score_list.append(line.score(graph))

    greedy_average_score = round(sum(greedy_score_list)/len(greedy_score_list))
    greedy_minn = sorted(greedy_score_list, reverse=False)[0]
    greedy_maxx = sorted(greedy_score_list, reverse=True)[0]
    greedy_sd = round(np.std(greedy_score_list))
    print(f"Greedy average_score = {greedy_average_score}")
    print(f"Greedy standard_deviation = {greedy_sd}")
    print(f"Greedy (Min, Max) = ({greedy_minn}, {greedy_maxx})")
