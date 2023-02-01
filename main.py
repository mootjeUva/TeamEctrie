# type: ignore
from code.classes.graph import Graph
from code.algorithms.randomise import Randomise
from code.algorithms.random_greedy import Random_Greedy
from code.algorithms.hillclimber import HillClimber
from code.algorithms.functions import runner, save_vis, csv_output, make_hist


if __name__ == "__main__":

    # Create graph and empty traject
    graph = Graph('data/StationsNationaal.csv',
                  'data/ConnectiesNationaal.csv')

    bestrandom, randlist = runner(graph, Randomise, 180, 20, 10000, False)
    save_vis(graph, bestrandom.line.lines, "best_random")
    csv_output(graph, bestrandom.line, "best_random")

    bestgreedy, greedylist = runner(graph, Random_Greedy, 180, 20, 10000, False)
    save_vis(graph, bestgreedy.line.lines, "best_greedy")
    csv_output(graph, bestgreedy.line, "best_greedy")

    hillclimb = HillClimber(graph, 180, bestgreedy)
    hillclimb.run(10000)
    save_vis(graph, hillclimb.best_state.line.lines, "best_hillclimber")
    csv_output(graph, hillclimb.best_state.line, "best_hillclimber")

    make_hist(randlist, greedylist, "Random", "Random-Greedy")
