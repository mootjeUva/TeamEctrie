# type: ignore
from code.classes.graph import Graph
from code.classes.traject import Traject
from folium import Map, Marker, PolyLine
import random
from matplotlib import colors


class Visualization():

    def __init__(self, graph: Graph) -> None:

        x = []
        y = []
        for name in graph.stations:
            x.append(graph.stations[name].x)
            y.append(graph.stations[name].y)

        mean_x = sum(x)/len(graph.stations)
        mean_y = sum(y)/len(graph.stations)
        self.map = Map(location=[mean_y, mean_x], tiles='cartodbpositron')
        self.map.fit_bounds([[min(y), min(x)], [max(y), max(x)]])

    def add_stations(self, graph: Graph) -> None:

        for name in graph.stations:
            Marker(location=[graph.stations[name].y, graph.stations[name].x],
                   popup=name).add_to(self.map)

    def add_traject(self, line: Traject, graph: Graph) -> None:

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
            point1 = [station1.y, station1.x]
            point2 = [station2.y, station2.x]
            PolyLine([point1, point2], color=color).add_to(self.map)

    def save_output(self, name: str) -> None:

        self.map.save('{}_map.html'.format(name))
