# type: ignore
from code.classes.graph import Graph
from code.algorithms.randomise import Randomise
from code.algorithms.greedy import RandomGreedy
from code.algorithms.greedy2 import Greedy2
from code.algorithms.hillclimber import HillClimber
from code.visualisation.visualise import Visualization
import numpy as np
import csv


if __name__ == "__main__":

    # Create graph and empty traject
    graph = Graph('data/StationsNationaal.csv',
                  'data/ConnectiesNationaal.csv')

    def runner(graph: Graph, Algo, timeframe: int,
               max_traject: int, iter: int, bool: bool):
        bestscore = 0
        scorelist = []

        for i in range(iter):
            algor = Algo(graph, timeframe, max_traject)
            algor.run()
            if algor.line.score(graph) > bestscore:
                bestscore = algor.line.score(graph)
                bestalgo = algor

            scorelist.append(algor.line.score(graph))

        averagescore = round(sum(scorelist)/len(scorelist), 2)
        minn = sorted(scorelist, reverse=False)[0]
        maxx = sorted(scorelist, reverse=True)[0]
        standard_deviation = round(np.std(scorelist))
        if bool is True:
            print(f"average_score = {averagescore}")
            print(f"standard_deviation = {standard_deviation}")
            print(f"(Min, Max) = ({minn}, {maxx})")

        return bestalgo

    def save_vis(graph: Graph, lines, str_name: str) -> None:

        vis = Visualization(graph)
        vis.add_stations(graph)
        for line in lines:
            vis.add_traject(line, graph)
        vis.save_output(str_name)

    bestrandom = runner(graph, Randomise, 180, 20, 2, False)
    bestrandomgreedy = runner(graph, RandomGreedy, 180, 20, 2, False)
    bestgreedy2 = runner(graph, Greedy2, 180, 20, 5000, False)
    
    #hillclimb = HillClimber(graph, 180, bestgreedy2)
    #hillclimb.run(2)

    save_vis(graph, bestrandom.line.lines, "best_random")
    save_vis(graph, bestrandomgreedy.line.lines, "best_random-greedy")
    save_vis(graph, bestgreedy2.line.lines, "best_greedy2")
    #save_vis(graph, hillclimb.best_state.line.lines, "best_hillclimber")


    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])
        i = 1
        for lin in bestgreedy2.line.lines:
            formatted_lin = ", ".join([str(item).replace("'", "") for item in lin])
            writer.writerow([f"train_{i}", f"[{formatted_lin}]"])
            i += 1
        writer.writerow([f"score", f"{bestgreedy2.line.score(graph)}"])
