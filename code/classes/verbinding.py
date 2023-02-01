class Connection():
    """ The Connection class represents a connection between two stations
        and the distance between them. """

    def __init__(self, station1: str, station2: str, distance: int) -> None:
        """ The constructor initializes the instance variables station1,
            station2, distance, connection_set and is_visited. """

        self.station1 = station1  # name of the first station (type: str)
        self.station2 = station2  # name of the second station (type: str)
        self.distance = distance  # distance between the two stations
        self.connection_set = {self.station1, self.station2}
        self.is_visited = False  # flag to check if the connection is visited
