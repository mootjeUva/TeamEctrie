# type: ignore
from code.classes.graph import Graph
from code.classes.lines import Lines
from code.visualisation.visualise import Visualization
import numpy as np
import csv
import matplotlib.pyplot as plt


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

    return bestalgo, scorelist


def save_vis(graph: Graph, lines, str_name: str) -> None:

    vis = Visualization(graph)
    vis.add_stations(graph)
    for line in lines:
        vis.add_traject(line, graph)
    vis.save_output(str_name)


def csv_output(graph: Graph, line: Lines, name: str) -> None:

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

    plt.hist(list1, color="red", edgecolor="black", hatch="\\", alpha=0.7)
    plt.hist(list2, color="blue", edgecolor="black", hatch="//", alpha=0.7)
    # Labels and title
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.title(f"The results of the {name1} and {name2} Algorithm done {len(list1)} times.")
    plt.legend(labels=[f"{name1}", f"{name2}"], loc="upper right")

    # Save the plot as a pdf
    plt.savefig("docs/histogram.pdf", bbox_inches="tight")
