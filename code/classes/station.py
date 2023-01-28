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

    def get_nearest_unvisited_station(self, graph: Any) -> Any:
        """ Method returns nearest unvisited station of a station. """

        # Create empty unvisited dict
        unvisited_stations_dict: Dict[str, int] = {}

        # Add all unvisited connected stations to dict with corresponding
        # distance as value
        for key in self.connections.keys():
            if graph.stations[key].is_visited is False:
                unvisited_stations_dict[key] = self.connections[key]

        # Check if dict is empty
        if not unvisited_stations_dict:
            return False

        else:
            # Find station with shortest distance
            nearest_con = min(unvisited_stations_dict,
                              key=unvisited_stations_dict.get)
            return nearest_con, unvisited_stations_dict[nearest_con]
        
    def get_nearest_unvisited_connection(self, graph):
        """
        Returns nearest unvisited connection
        """ 
        # Create empty connection dict
        connection_dict: Dict[Connection, list[str, int]]= {}

        for connection in self.connections_list:
            if connection.is_visited is False:
                # Add connection object to connection dict with the distance as its value
                connection_dict[connection] = [str(connection.connection_set.difference(self)), self.connections[connection]]

        # Check if dict is empty
        if not connection_dict:
            return False
        else:
            # Find connection with shortest distance
            nearest_con = min(connection_dict,
                              key=connection_dict.get)
            connected_station = connection_dict[nearest_con][0]
            # Return connected_station, connection object, distance to connected station
            return connected_station, nearest_con, self.connections[connected_station]







    def __repr__(self) -> str:
        return self.name
