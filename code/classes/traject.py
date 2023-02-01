from typing import List, Set


class Traject():
    """ The Traject class is used to keep track of a particular route
        taken by a user between multiple stations. """

    def __init__(self) -> None:
        """ The constructor initializes the list of stations,
            total_distance traveled, ridden_connections and variables i,
            and j. """

        self.stations: List[str] = []  # list to keep track of stations
        self.total_distance: int = 0  # variable of the total distance
        self.ridden_connections: List[Set[str]] = []  # ridden connections list
        self.i: int = 0  # variable i
        self.j: int = 0  # variable j

    def add_station(self, station: str, distance: int) -> None:
        """ This method adds a station to the route and updates
            the total_distance traveled so far. """

        self.stations.append(station)  # add station to list of stations
        if self.j == 0:
            self.j = 1
            return
        else:
            self.total_distance += distance

    def add_connection(self, connection_set: Set[str]) -> None:
        """ This method adds a connection to the route and updates the
            ridden_connections list. """

        if self.i == 0:
            self.i = 1
            return
        else:
            self.ridden_connections.append(connection_set)
