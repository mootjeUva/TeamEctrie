# type: ignore
from code.classes.graph import Graph
from code.algorithms.randomise import Randomise
import numpy as np
from code.algorithms.greedy import RandomGreedy
# from code.visualisation.visualise import Visualization
from code.algorithms.hillclimber import HillClimber



if __name__ == "__main__":

    # Create graph and empty traject
    # graph = Graph('data/StationsNationaal.csv',
    #               'data/ConnectiesNationaal.csv')

    # -------------------------Random Algorithm-------------------------
    # best_randomscore = 0
    # best_randomline = []
    # random_score_list = []

    # for j in range(1000):
    #     rd = Randomise(graph, 180, 20)
    #     rd.run()
    #     if rd.line.score(graph) > best_randomscore:
    #         best_randomscore = rd.line.score(graph)
    #         best_randomline = rd.line.lines

    #     random_score_list.append(rd.line.score(graph))

    # random_average_score = round(sum(random_score_list)/len(random_score_list))
    # random_minn = sorted(random_score_list, reverse=False)[0]
    # random_maxx = sorted(random_score_list, reverse=True)[0]
    # random_standard_deviation = round(np.std(random_score_list))
    # print(f"Random average_score = {random_average_score}")
    # print(f"Random standard_deviation = {random_standard_deviation}")
    # print(f"Random (Min, Max) = ({random_minn}, {random_maxx})")

    # # vis = Visualization(graph)
    # # vis.add_stations(graph)
    # # for line in best_randomline:
    # #     vis.add_traject(line, graph)
    # # vis.save_output('best_random')

    # # ---------------------------RandomGreedy Algorithm-----------------------
    # best_greedy_score = 0
    # best_greedy_line = []
    # greedy_score_list = []

    # for i in range(1000):
    #     graph = Graph('data/StationsNationaal.csv',
    #                   'data/ConnectiesNationaal.csv')
    #     gr = RandomGreedy(graph, 180, 20)
    #     gr.run()
    #     if gr.line.score(graph) > best_greedy_score:
    #         best_greedy_score = gr.line.score(graph)
    #         best_greedy_line = gr.line.lines
    #     greedy_score_list.append(gr.line.score(graph))

    # greedy_average_score = round(sum(greedy_score_list)/len(greedy_score_list))
    # greedy_minn = sorted(greedy_score_list, reverse=False)[0]
    # greedy_maxx = sorted(greedy_score_list, reverse=True)[0]
    # greedy_sd = round(np.std(greedy_score_list))
    # print(f"Greedy average_score = {greedy_average_score}")
    # print(f"Greedy standard_deviation = {greedy_sd}")
    # print(f"Greedy (Min, Max) = ({greedy_minn}, {greedy_maxx})")

    # vis2 = Visualization(graph)
    # vis2.add_stations(graph)
    # for line in best_greedy_line:
    #     vis2.add_traject(line, graph)
    # vis2.save_output('best_greedy')

    #--------------------------HillClimber Albgorithm-----------------------------

     graph = Graph('data/StationsNationaal.csv',
                 'data/ConnectiesNationaal.csv')
    
     gr = RandomGreedy(graph, 180, 20)
     gr.run()
     print(gr.line.score(graph))
     hillclimb = HillClimber(graph,180, gr)
     hillclimb.run(10000)    
     print(hillclimb.best_state.line.score(graph))  
    
    
    # best_hillclimber_score = 0
    # best_hillclimber_line = []
    # hillclimber_score_list = []

    # for i in range(1000):
    #     hc = HillClimber(graph, gr.line, 180)
    #     hc.run()
    #     if hc.best_line.score(graph) > best_hillclimber_score:
    #         best_hillclimber_score = hc.best_line.score(graph)
    #         best_hillclimber_line = hc.best_line.lines

    # hillclimber_average_score = round(sum(hillclimber_score_list)/len(hillclimber_score_list))
    # hillclimber_minn = sorted(hillclimber_score_list, reverse=False)[0]
    # hillclimber_maxx = sorted(hillclimber_score_list, reverse=True)[0]
    # hillclimber_sd = round(np.std(hillclimber_score_list))
    # print(f"hillclimber average_score = {hillclimber_average_score}")
    # print(f"hillclimber standard_deviation = {hillclimber_sd}")
    # print(f"hillclimber (Min, Max) = ({hillclimber_minn}, {hillclimber_maxx})")