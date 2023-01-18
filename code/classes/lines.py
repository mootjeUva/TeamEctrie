from .traject import Traject


class Lines():

    def __init__(self) -> None:

        self.lines = []
        self.distances = []

    def add_traject(self, traject: Traject) -> None:

        train_list = list(traject.stations.keys())

        if train_list not in self.lines:
            self.lines.append(train_list)
            self.distances.append(traject.total_distance)

    def score(self) -> float:

        T = len(self.lines)
        Min = sum(self.distances)
        p = 1
        K = p*10000 - (T*100 + Min)

        return K
