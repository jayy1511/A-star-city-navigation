from City import City

class Map:
    def __init__(self, filename="FRANCE.MAP"):
        self.cities = {}
        self.load_map(filename)

    def load_map(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                current_city = None
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 3:  # It's a city with coordinates
                        name, x, y = parts
                        current_city = City(name, int(x), int(y))
                        self.cities[name] = current_city
                    elif len(parts) == 2:  # It's a neighboring city with distance
                        neighbor_name, distance = parts
                        if current_city:
                            current_city.add_neighbor(neighbor_name, int(distance))
        except FileNotFoundError:
            print("Data file not found")
            exit(2)

    def get_city(self, name):
        return self.cities.get(name, None)

    def __repr__(self):
        return f"Map({self.cities})"
