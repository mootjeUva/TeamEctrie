from typing import Dict


class Traject():

    def __init__(self) -> None:
        self.stations: Dict[str, int] = {}
        self.total_distance = 0

    def add_station(self, station: str, distance: int) -> None:
        
            self.stations[station] = distance
            self.total_distance += distance
