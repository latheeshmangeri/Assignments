import sys
from queue import PriorityQueue


class Node:
    def __init__(self, city, cost=0, path=None):
        self.city = city
        self.cost = cost
        self.path = path if path else []


def read_input_file(input_filename):
    graph = {}
    with open(input_filename, 'r') as file:
        for line in file:
            if line.strip() == "END OF INPUT":
                break
            source, destination, length = line.strip().split()
            if source not in graph:
                graph[source] = {}
            if destination not in graph:
                graph[destination] = {}
            graph[source][destination] = float(length)
            graph[destination][source] = float(length)
    return graph


def read_heuristic_file(heuristic_filename):
    heuristic = {}
    with open(heuristic_filename, 'r') as file:
        for line in file:
            if line.strip() == "END OF INPUT":
                break
            city, h_value = line.strip().split()
            heuristic[city] = float(h_value)
    return heuristic


def uninformed_search(graph, origin_city, destination_city):
    print('\nUninformed Cost Search Strategy')
    fringe = PriorityQueue()
    fringe.put((0, Node(origin_city)))
    visited = set()
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1

    while not fringe.empty():
        _, current = fringe.get()
        nodes_popped += 1

        if current.city == destination_city:
            return current.path + [current.city], nodes_popped, nodes_expanded, nodes_generated

        if current.city not in visited:
            visited.add(current.city)

            children = graph.get(current.city)
            if children:
                nodes_expanded += 1

            for next_city, cost in children.items():
                nodes_generated += 1
                fringe.put((current.cost + cost, Node(next_city, path=current.path + [current.city], cost=current.cost + cost)))
    return None, nodes_popped, nodes_expanded, nodes_generated


def informed_search(graph, origin_city, destination_city, heuristic):
    print('\nA* Search Strategy')
    fringe = PriorityQueue()
    fringe.put((0, Node(origin_city)))
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1

    while not fringe.empty():
        _, current = fringe.get()
        nodes_popped += 1

        if current.city == destination_city:
            return current.path + [current.city], nodes_popped, nodes_expanded, nodes_generated

        nodes_expanded += 1
        for next_city in graph[current.city]:
            nodes_generated += 1
            if next_city not in current.path:
                new_cost = current.cost + graph[current.city][next_city]
                priority = new_cost + heuristic[next_city]
                fringe.put((priority, Node(next_city, new_cost, current.path + [current.city])))
    print('info')
    return None, nodes_popped, nodes_expanded, nodes_generated


def print_route(graph, route):
    if route is None:
        print("Route: Infinity\n")
    else:
        total_distance = 0
        route_str = "Route:\n"
        for i in range(len(route) - 1):
            distance = graph[route[i]][route[i + 1]]
            total_distance += distance
            route_str += f"{route[i]} to {route[i + 1]}, {distance} km\n"
        route_str += f"Total Distance: {total_distance} km\n"
        print(route_str)


def find_route():
    input_filename = sys.argv[1]
    origin_city = sys.argv[2]
    destination_city = sys.argv[3]

    graph = read_input_file(input_filename)

    if len(sys.argv) == 5:
        heuristic_filename = sys.argv[4]
        heuristic = read_heuristic_file(heuristic_filename)
        path, nodes_popped, nodes_expanded, nodes_generated = informed_search(graph, origin_city, destination_city, heuristic)
    else:
        path, nodes_popped, nodes_expanded, nodes_generated = uninformed_search(graph, origin_city, destination_city)

    print(f"Nodes Popped: {nodes_popped}")
    print(f"Nodes Expanded: {nodes_expanded}")
    print(f"Nodes Generated: {nodes_generated}")
    if path is not None:
        print(f"Distance: {sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))} km")
    print_route(graph, path)


if __name__ == "__main__":
    try:
        find_route()
    except:
        print('\nusage for uninformed search: python3 find_route.py input1.txt Bremen Kassel')
        print('\nusage for Informed search: python3 find_route.py input1.txt Bremen Kassel h_kassel.txt\n')
    