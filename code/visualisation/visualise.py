# type: ignore
from code.classes.graph import Graph
from code.classes.traject import Traject
from folium import Map, Marker, PolyLine
import random
from matplotlib import colors


class Visualization:
    """ The Visualization class creates a visual representation of the graph
        and trajects. """

    def __init__(self, graph: Graph) -> None:
        """ Initialize the Visualization class by computing the mean x and
            y values of the stations in the graph, and creating an instance
            of folium Map centered at these mean values. """

        self.i = 0  # counter for number of trains
        x = []  # list of x-coordinates of stations
        y = []  # list of y-coordinates of stations
        for name in graph.stations:
            x.append(graph.stations[name].x)
            y.append(graph.stations[name].y)

        mean_x = sum(x)/len(graph.stations)
        mean_y = sum(y)/len(graph.stations)
        # create a folium map object centered around the mean x
        # and y of the stations
        self.map = Map(location=[mean_y, mean_x], tiles='cartodbpositron')
        # fit the map bounds to show all the stations
        self.map.fit_bounds([[min(y), min(x)], [max(y), max(x)]])

    def add_stations(self, graph: Graph) -> None:
        """ This method adds markers to the folium map instance for each
            station in the graph. """

        for name in graph.stations:
            # add a marker to the map for each station
            Marker(location=[graph.stations[name].y, graph.stations[name].x],
                   popup=name).add_to(self.map)

    def add_traject(self, line: Traject, graph: Graph) -> None:
        """ This method adds a colored polyline to the folium map instance
            for each station in a given Traject. """

        self.i += 1  # increment the train counter
        # generate a random color for the train line
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = colors.rgb2hex((r/255, g/255, b/255))
        x = []
        for name in line:
            x.append(graph.stations[name])
        for i in range(len(x) - 1):
            station1 = x[i]
            station2 = x[i+1]
            points = [[station1.y, station1.x], [station2.y, station2.x]]
            # add a polyline to the map representing the train line
            PolyLine(points, color=color,
                     popup='train_{}'.format(self.i)).add_to(self.map)

    def save_output(self, name: str) -> None:
        """ This method saves the folium map instance to an HTML file
            with a given name. """

        self.map.save('docs/{}_map.html'.format(name))
