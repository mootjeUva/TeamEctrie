from typing import Dict, List, Any
from .verbinding import Connection


class Station():

    def __init__(self, station: str, x: float, y: float) -> None:

        self.name = station
        self.x = x
        self.y = y
        self.connections: Dict[str, int] = {}
        self.is_visited = False
        self.connections_list: List[Connection] = []

    def add_connection(self, station: str, distance: int) -> None:

        self.connections[station] = distance
        self.connections_list.append(Connection(self.name, station, distance))

    def get_connection(self) -> List[Connection]:

        return self.connections_list

    def highest_potential(self, graph: Any) -> Any:
        """ This method returns a visited connection which has by itself
            unvisited connections, else returns false. """

        # Loops over all visited connections of self
        for visited in self.connections.keys():
            # Loops over all connections of the visited connections
            for potential in graph.stations[visited].connections.keys():
                # Check if there is any connection which isn't visited yet
                if graph.stations[potential].is_visited is False:
                    # Return the (already visited) station which has by itself
                    # an unvisited connection
                    return visited
        else:
            return False

    def get_nearest_unvisited_connection(self, graph: Any) -> Any:
        """ Method returns nearest unvisited connection of a station. """

        # Create empty unvisited dict
        unvisited_connections_dict: Dict[str, int] = {}

        # Add all unvisited connected stations to dict with corresponding
        # distance as value
        for key in self.connections.keys():
            if graph.stations[key].is_visited is False:
                unvisited_connections_dict[key] = self.connections[key]

        # Check if dict is empty
        if not unvisited_connections_dict:
            return False

        else:
            # Find connection with shortest distance
            nearest_con = min(unvisited_connections_dict,
                              key=unvisited_connections_dict.get)
            return nearest_con, unvisited_connections_dict[nearest_con]

    def __repr__(self) -> str:
        return self.name
