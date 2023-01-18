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
        p = self.compute_p()
        K = p*10000 - (T*100 + Min)

        return K
    
    def compute_p(self):
        total_stations = 0

        # Count how many stations in total are reached in self.lines
        for i in range(len(self.lines)):
            total_stations += len(self.lines[i])

        # connections / total connections
        p = round((total_stations - 1) / 28)

        return p
