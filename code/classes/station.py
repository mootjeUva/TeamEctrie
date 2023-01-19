from typing import Dict, List
from .verbinding import Connection


class Station():

    def __init__(self, station: str, x: float, y: float) -> None:

        self.name = station
        self.x = x
        self.y = y
        self.connections: Dict[str, int] = {}
<<<<<<< HEAD
        self.is_visited = False
=======
        self.connections_list: List[Connection] = []
>>>>>>> 59fa8a75d3301a5402c8e608d1c7454a810d7602

    def add_connection(self, station: str, distance: int) -> None:

        self.connections[station] = distance
        self.connections_list.append(Connection(self.name, station, distance))

    def get_connection(self) -> List[Connection]:

        return self.connections_list

    def __repr__(self) -> str:

        return self.name
