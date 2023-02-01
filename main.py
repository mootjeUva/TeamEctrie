# type: ignore
from code.classes.graph import Graph
from code.algorithms.randomise import Randomise
from code.algorithms.random_greedy import Random_Greedy
from code.algorithms.hillclimber import HillClimber
from code.algorithms.functions import runner, save_vis, csv_output, make_hist
import random


if __name__ == "__main__":

    # Create graph and empty traject
    graph = Graph('data/StationsNationaal.csv',
                  'data/ConnectiesNationaal.csv')

    # Set the seed for the random number generator for repeatable results
    random.seed(79)
    # Call the runner function to run the Randomise algorithm
    # for 1000 iterations. The runner function returns the best
    # algorithm and a list of all the scores
    bestrandom, randlist = runner(graph, Randomise, 180, 20, 1000, False)
    # Save the visualization of the best result to a file
    save_vis(graph, bestrandom.line.lines, "best_random")
    # Save the output to a CSV file
    csv_output(graph, bestrandom.line, "best_random")

    # Set the seed for the random number generator for repeatable results
    random.seed(17)
    # Call the runner function to run the Random_Greedy algorithm
    # for 1000 iterations. The runner function returns the best
    # algorithm and a list of all the scores
    bestgreedy, greedylist = runner(graph, Random_Greedy, 180, 20, 1000, False)

    # Initialize the HillClimber algorithm with the graph and
    # the best result from the Random_Greedy algorithm
    hillclimb = HillClimber(graph, 180, bestgreedy)
    # Run the HillClimber algorithm for 1000 iterations
    hillclimb.run(1000)

    # Save the visualization of the best result to a file
    save_vis(graph, bestgreedy.line.lines, "best_greedy")
    # Save the result from the Random_Greedy algorithm to a CSV file
    csv_output(graph, bestgreedy.line, "best_greedy")
    # Save the visualization of the best result to a file
    save_vis(graph, hillclimb.best_state.line.lines, "best_hillclimber")
    # Save the result from the HillClimber algorithm to a CSV file
    csv_output(graph, hillclimb.best_state.line, "best_hillclimber")

    # Create a histogram comparing the results
    # from the Randomise and Random_Greedy algorithms
    make_hist(randlist, greedylist, "Random", "Random-Greedy")
