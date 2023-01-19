from typing import Dict, List
from .verbinding import Connection


class Station():

    def __init__(self, station: str, x: float, y: float) -> None:

        self.name = station
        self.x = x
        self.y = y
        self.connections: Dict[str, int] = {}
        self.connections_list: List[Connection] = []

    def add_connection(self, station: str, distance: int) -> None:

        self.connections[station] = distance
        self.connections_list.append(Connection(self.name, station, distance))

    def get_connection(self) -> list:

        return self.connections_list

    def __repr__(self) -> str:

        return self.name
