class Connection():

    def __init__(self, station1: str, station2: str, distance: int) -> None:

        self.station1 = station1
        self.station2 = station2
        self.distance = distance
        self.connection_set = {self.station1, self.station2}

    # def __repr__(self) -> str:

    #     return f"{self.station1}, {self.station2}, {self.distance}"
