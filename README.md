# A* Shortest Path Algorithm

This project implements the A* algorithm to compute the shortest path between two cities based on a predefined map of France. The map data, including city names, coordinates, and distances, is provided in a text file.

## Table of Contents
- [Overview](#overview)
- [Files](#files)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Complexity](#complexity)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Overview
The A* algorithm is a popular pathfinding and graph traversal algorithm used to find the shortest path between nodes. This implementation reads map data from a file and calculates the shortest path between two specified cities.

## Files
- `City.py`: Contains the `City` class, representing each city with its coordinates and neighbors.
- `Map.py`: Contains the `Map` class, responsible for loading and managing the map data.
- `a_star.py`: Contains the implementation of the A* algorithm.
- `main.py`: The main entry point of the program.
- `FRANCE.MAP`: The map data file.
- `Complexity_Evaluation.txt`: Evaluation of the algorithm's complexity.
- `README.md`: This file.

## Usage
Run the program from the command line:
```sh
python main.py <start_city> <goal_city>
