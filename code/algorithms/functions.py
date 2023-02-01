# type: ignore
from code.classes.graph import Graph
from code.classes.lines import Lines
from code.visualisation.visualise import Visualization
import numpy as np
import csv
import matplotlib.pyplot as plt


def runner(graph: Graph, Algo, timeframe: int,
           max_traject: int, iter: int, bool: bool):
    """ This function runs the algorithm that is given as an argument. """

    # Define bestscore and scorelist
    bestscore = 0
    scorelist = []

    # Runs the algorithm for iter times
    for i in range(iter):
        # Create algorithm object
        algor = Algo(graph, timeframe, max_traject)
        # Run the algorithm
        algor.run()
        # If the objects score is higher than bestscore,
        # adjust bestscore and bestalgo
        if algor.line.score(graph) > bestscore:
            bestscore = algor.line.score(graph)
            bestalgo = algor

        # Keep track of all the generated scores in the scorelist
        scorelist.append(algor.line.score(graph))

    # Determine important statistics
    averagescore = round(sum(scorelist)/len(scorelist), 2)
    minn = sorted(scorelist, reverse=False)[0]
    maxx = sorted(scorelist, reverse=True)[0]
    standard_deviation = round(np.std(scorelist))

    # If bool is True print the statistics
    if bool is True:
        print(f"average_score = {averagescore}")
        print(f"standard_deviation = {standard_deviation}")
        print(f"(Min, Max) = ({minn}, {maxx})")

    return bestalgo, scorelist


def save_vis(graph: Graph, lines, str_name: str) -> None:
    """ Function that creates a visualisation of a line. """

    vis = Visualization(graph)
    vis.add_stations(graph)
    for line in lines:
        vis.add_traject(line, graph)
    vis.save_output(str_name)


def csv_output(graph: Graph, line: Lines, name: str) -> None:
    """ Function writes line and score to a csv file. """

    with open(f"results/{name}_output.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])
        i = 1
        for lin in line.lines:
            lin2 = ", ".join([str(item).replace("'", "") for item in lin])
            writer.writerow([f"train_{i}", f"[{lin2}]"])
            i += 1
        writer.writerow(["score", f"{line.score(graph)}"])


def make_hist(list1: list, list2: list, name1: str, name2: str) -> None:
    """ Function creates histograms. """

    plt.hist(list1, color="red", edgecolor="black", hatch="\\", alpha=0.7)
    plt.hist(list2, color="blue", edgecolor="black", hatch="//", alpha=0.7)
    # Labels and title
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.title("The results of the " + name1 + " and " + name2 +
              " Algorithm done " + str(len(list1)) + " times.")
    plt.legend(labels=[f"{name1}", f"{name2}"], loc="upper right")

    # Save the plot as a pdf
    plt.savefig("docs/histogram.pdf", bbox_inches="tight")
