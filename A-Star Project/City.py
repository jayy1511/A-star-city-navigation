class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = {}

    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance

    def __repr__(self):
        return f"City({self.name}, {self.x}, {self.y}, {self.neighbors})"
