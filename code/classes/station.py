from typing import Dict


class Station():

    def __init__(self, station: str, x: float, y: float) -> None:

        self.name = station
        self.x = x
        self.y = y
        self.connections: Dict[str, int] = {}
        self.is_visited = False

    def add_connection(self, station: str, distance: int) -> None:

        self.connections[station] = distance

    def get_connection(self) -> Dict[str, int]:

        return self.connections

    def __repr__(self) -> str:

        return self.name
