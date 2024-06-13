import sys
from Map import Map
from a_Star import a_star, print_path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        start_name = input("Enter the start city: ")
        goal_name = input("Enter the goal city: ")
    else:
        start_name = sys.argv[1]
        goal_name = sys.argv[2]

    map = Map()
    path = a_star(map, start_name, goal_name)
    print_path(path, map)
    sys.exit(0)
