from typing import Dict


class Traject():

    def __init__(self, timeframe: int) -> None:

        self.timeframe = timeframe
        self.stations: Dict[str, int] = {}
        self.total_distance = 0

    def add_station(self, station: str, distance: int) -> None:

        if self.total_distance + distance < self.timeframe:
            self.stations[station] = distance
            self.total_distance += distance
