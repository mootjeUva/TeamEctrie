from typing import Dict, List, Any
from .verbinding import Connection


class Station():
    """ Class Station is used to create station objects which contain
        information about the station's name, position (x, y),
        connections to other stations and whether it has been visited. """

    def __init__(self, station: str, x: float, y: float) -> None:
        """ This method is used to initialize the Station object with the
            station's name, position (x, y), and empty data structures for
            connections, visited status, list of connections,
            and dictionary of connection objects. """

        self.name = station
        self.x = x
        self.y = y
        self.connections: Dict[str, int] = {}
        self.is_visited = False
        self.connections_list: List[Connection] = []
        self.connection_objects_dict: Dict[str, Connection] = {}

    def add_connection(self, station: str, distance: int,
                       connection: Connection) -> None:
        """ Method add_connection is used to add a new connection to a station.
            The connection is added as a key-value pair to the connections
            dictionary and as an object to the connections_list and
            connection_objects_dict. """

        self.connections[station] = distance
        if connection not in self.connections_list:
            self.connections_list.append(connection)
        self.connection_objects_dict[station] = connection

    def get_connection_object(self, station: str) -> Any:
        """ This method returns the connection object between
            the station and the given station. """

        return self.connection_objects_dict[station]

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

    def get_nearest_unvisited_connection(self) -> Any:
        """ Returns nearest unvisited connection. """

        # Create empty connection dict
        connection_dict: Dict[Connection, List[Any]] = {}

        for connection in self.connections_list:
            if connection.is_visited is False:
                # Add connection object to connection dict
                # with the distance as its value
                tmp_con_list = list(connection.connection_set)
                tmp_con_list.remove(self.name)
                connection_dict[connection] = [tmp_con_list[0],
                                               connection.distance]

        # Check if dict is empty
        if not connection_dict:
            return False
        else:
            # Find connection with shortest distance
            tmp = 1000
            nearest_con = ''
            for con in connection_dict:
                if con.distance < tmp:
                    tmp = con.distance
                    nearest_con = con

            connected_station = connection_dict[nearest_con][0]
            distance = self.connections[connected_station]
            con_object = self.get_connection_object(connected_station)
            # Return connected_station, connection object,
            # distance to connected station
            return connected_station, con_object, distance

    def get_highest_potential_connection(self, graph: Any, tmp: Any) -> Any:
        """ Returns highest potential connection. """

        connected_stations = []

        # Find connected stations
        for station in self.connections.keys():
            connected_stations.append(station)

        if tmp in connected_stations:
            connected_stations.remove(tmp)

        if not connected_stations:
            return False

        # Loop over stations in connected stations
        for station in connected_stations:
            # Loop over the connections of the connected stations
            for i in range(len(graph.stations[station].connections_list)):
                # Check if that connection isn't visited yet
                if graph.stations[
                                  station
                                 ].connections_list[i].is_visited is False:
                    # If not visited yet, return station and distance
                    # (connection isn't important because the connection
                    # is already visited)
                    return station, self.connections[station]
        return False
