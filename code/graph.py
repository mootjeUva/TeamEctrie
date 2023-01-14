import csv
from verbinding import Connection
from station import Station

class Graph():
    def __init__(self, station_file, connection_file):
        self.stations = self.load_stations(station_file)
        self.connections = self.load_connections(connection_file)


    def load_stations(self, source_file: str) -> dict:
        """
        Load all stations into the graph
        """
        stations = {}

        with open(source_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Read station name, x-coordinate and y-coordinate from reader
                name = row['station']
                x_value = row['x']
                y_value = row['y']
                # Create station and append to stations list
                stations[name] = Station(name, x_value, y_value)

        return stations

    def load_connections(self, source_file: str) -> dict:
        """
        Load all connections into the graph
        """
        # Create a connections dict where every key is station1 and value is a list of station 2 and the distance to it
        connections: dict[str, list[str, int]] = {}

        with open(source_file, 'r') as file:
            reader = csv.DictReader(file)

            # Connect station 1 to station 2 and vice versa
            for row in reader:
                # Create connection
                connection = Connection(row['station1'], row['station2'], row['distance'])
                # Add connection to specific station
                self.stations[connection.station1].add_connection(connection.station2, connection.distance)
                # Add connection to connections dict
                connections[connection.station1] = [connection.station2, connection.distance]

        return connections

#__________Code to test if the the graph is working correctly___________

# def main():
#     graph = Graph('../data/StationsHolland.csv', '../data/ConnectiesHolland.csv')
#     print(graph.connections)


# if __name__ == "__main__":
#     main()