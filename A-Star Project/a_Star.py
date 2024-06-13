import math
from queue import PriorityQueue
from Map import Map

def heuristic(city1, city2):
    return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2)

def a_star(map, start_name, goal_name):
    start_city = map.get_city(start_name)
    goal_city = map.get_city(goal_name)
    if not start_city or not goal_city:
        print("Unknown city name")
        exit(1)

    open_set = PriorityQueue()
    open_set.put((0, start_name))
    came_from = {}
    g_score = {city: float('inf') for city in map.cities}
    g_score[start_name] = 0
    f_score = {city: float('inf') for city in map.cities}
    f_score[start_name] = heuristic(start_city, goal_city)

    while not open_set.empty():
        _, current_name = open_set.get()
        current_city = map.get_city(current_name)
        if current_name == goal_name:
            return reconstruct_path(came_from, current_name)

        for neighbor_name, distance in current_city.neighbors.items():
            tentative_g_score = g_score[current_name] + distance
            if tentative_g_score < g_score[neighbor_name]:
                came_from[neighbor_name] = current_name
                g_score[neighbor_name] = tentative_g_score
                f_score[neighbor_name] = tentative_g_score + heuristic(map.get_city(neighbor_name), goal_city)
                open_set.put((f_score[neighbor_name], neighbor_name))

    print("No path found")
    exit(3)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def print_path(path, map):
    total_distance = 0
    for i in range(len(path)):
        if i == 0:
            print(f"{path[i]} : (0 km)")
        else:
            prev_city = map.get_city(path[i-1])
            current_city = map.get_city(path[i])
            distance = prev_city.neighbors[path[i]]
            total_distance += distance
            print(f"{path[i]} : ({total_distance} km)")
