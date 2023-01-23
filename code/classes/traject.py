from .verbinding import Connection
from typing import Dict, List


class Traject():

    def __init__(self) -> None:

        self.stations: list[str] = []
        self.total_distance = 0
        self.ridden_connections: List[set[str, str]] = []

    def add_station(self, station: str, distance: int) -> None:

        self.stations.append(station)
        self.total_distance += distance

    def add_connection(self, connection_set: set[str, str]) -> None:

        self.ridden_connections.append(connection_set)

    def __str__(self) -> str:

        return f'{[station for station in self.stations]}'

    def check_timeframe(self, distance: int) -> bool:

        if self.total_distance + distance < 120:
            return True
        else:
            return False
