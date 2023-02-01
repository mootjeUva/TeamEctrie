import csv
from .verbinding import Connection
from .station import Station
from typing import Dict, List, Any


class Graph():
    """ Class representing a graph data structure of the metro system. """

    def __init__(self, station_file: str, connection_file: str) -> None:
        """ Initialize the Graph instance. """

        # Load all the stations into the graph
        self.stations = self.load_stations(station_file)
        # A list of all connections in the graph
        self.all_connections: List[Connection] = []
        # Load all connections into the graph
        self.connections = self.load_connections(connection_file)
        # A dictionary mapping connection objects to their str representation
        self.connection_object_dict: Dict[str, Connection] = {}

    def load_stations(self, source_file: str) -> Dict[str, Station]:
        """ Load all stations into the graph. """

        stations = {}

        with open(source_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Read station name, x-coordinate and y-coordinate from reader
                name = row['station']
                x_value = float(row['x'])
                y_value = float(row['y'])
                # Create station and append to stations list
                stations[name] = Station(name, x_value, y_value)

        return stations

    def load_connections(self, source_file: str) -> Dict[str, Dict[str, int]]:
        """ Load all connections into the graph. """

        # Create a connections dict where every key is station1
        # and the value is a list of station2 and the distance to it
        connections: Dict[str, Dict[str, int]] = {}

        with open(source_file, 'r') as file:
            reader = csv.DictReader(file)

            # Connect station 1 to station 2 and vice versa
            for row in reader:
                # Create connection
                connection = Connection(row['station1'],
                                        row['station2'],
                                        int(float(row['distance'])))

                self.all_connections.append(connection.connection_set)
                # Add connection to specific station in both ways
                self.stations[connection.station1].add_connection(
                                                    connection.station2,
                                                    connection.distance,
                                                    connection)
                self.stations[connection.station2].add_connection(
                                                    connection.station1,
                                                    connection.distance,
                                                    connection)
                # Add connection in connections dict both ways:
                # station 1 to station 2 and vice versa
                if connection.station1 not in connections.keys():
                    connections[connection.station1] = {connection.station2:
                                                        connection.distance}
                else:
                    connections[connection.station1].update(
                        {connection.station2: connection.distance})
                if connection.station2 not in connections.keys():
                    connections[connection.station2] = {connection.station1:
                                                        connection.distance}
                else:
                    connections[connection.station2].update(
                        {connection.station1: connection.distance})

        return connections

    def not_visited_yet(self, endpoint_stations: List[Any]) -> Any:
        """ This method returns an if possible an unvisited endpoint station,
            else an unvisited station. """

        # Check if there is any unvisited endpoint station in the graph
        for station in endpoint_stations:
            if self.stations[station].is_visited is False:
                return station

        # If no unvisited endpoint station, return a random unvisited station
        for station in self.connections.keys():
            if self.stations[station].is_visited is False:
                return station

        return False

    def endpoint_stations(self) -> List[Any]:
        """ This method returns a list of all stations with only one
            connection (endpoint stations). """

        endpoint_stations = []

        for station in self.stations.values():
            if len(self.connections[station.name].values()) == 1:
                endpoint_stations.append(station.name)

        return endpoint_stations
