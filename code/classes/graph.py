import csv
from .verbinding import Connection
from .station import Station
from typing import Dict, List, Any


class Graph():

    def __init__(self, station_file: str, connection_file: str) -> None:

        self.stations = self.load_stations(station_file)
        self.all_connections: List[Connection] = []
        self.connections = self.load_connections(connection_file)

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
                                        int(row['distance']))
                connection2 = Connection(row['station2'],
                                         row['station1'],
                                         int(row['distance']))

                self.all_connections.append(connection)
                self.all_connections.append(connection2)
                
                # Add connection to specific station
                self.stations[connection.station1].add_connection(
                                                    connection.station2,
                                                    connection.distance)
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

    def not_visited_yet(self, station: str) -> Any:
        """ This method returns a station from connections list if it is not
            visited yet, if all stations in connections are visited function
            returns False. """

        for option in self.connections[station].keys():
            if self.stations[option].is_visited is False:
                return option

        return False

    def distance_between_stations(self, station1: str, station2: str) -> int:
        """ This method returns the distance between two stations. """

        distance = self.connections[station1][station2]

        return distance
