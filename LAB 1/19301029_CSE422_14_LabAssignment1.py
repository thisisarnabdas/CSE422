def read_graph(filename):
    graph = {}          # Stores cities and distances from the other cities
    heuristics = {}     # Stores heuristics for each city    
    file = open(filename, 'r')
    for line in file:
        data = line.strip().split()
        city = data[0]
        heuristic_value = int(data[1])
        heuristics[city] = heuristic_value
        if city not in graph:
            graph[city] = {}
        connections = data[2:]
        for i in range(0, len(connections), 2):
            neighbour = connections[i]
            distance = int(connections[i + 1])
            if neighbour not in graph:
                graph[neighbour] = {}
            graph[city][neighbour] = distance
            graph[neighbour][city] = distance
            # print(graph)
    file.close()
    return graph, heuristics

def best_path(graph, heuristics, start, goal):
    paths_to_check = []
    initial_path = {
        'f_n': heuristics[start], # f(n) = g(n) + h(n)
        'g_n': 0,                 # g(n) = distance from start node
        'city': start,
        'path': [start]
    }
    paths_to_check.append(initial_path)
    visited_cities = set() 
    while paths_to_check:
        min_cost = float('inf')
        current_index = 0        
        for i, path in enumerate(paths_to_check): #checking ad selecting the lowest f(n)
            if path['f_n'] < min_cost:
                min_cost = path['f_n']
                current_index = i    
        current = paths_to_check.pop(current_index)
        current_city = current['city']
        if current_city == goal:
            return current['path'], current['g_n']
        if current_city in visited_cities:
            continue
        # visited_cities.add(current_city)
        for next_city, distance in graph[current_city].items(): #exploration of paths
            if next_city not in visited_cities:
                new_distance = current['g_n'] + distance
                new_score = new_distance + heuristics[next_city]                
                new_path = current['path'] + [next_city]
                new_path_data = {
                    'f_n': new_score,
                    'g_n': new_distance,
                    'city': next_city,
                    'path': new_path
                }
                paths_to_check.append(new_path_data)
        visited_cities.add(current_city)
    return None, None


graph, heuristics = read_graph('input.txt')
start = input("Start node: ")
goal = input("Destination: ")
path, total_distance = best_path(graph, heuristics, start, goal)
if path:
    print("\nPath: ", end="")
    print(" -> ".join(path))
    print(f"Total distance: {total_distance} km")
else:
    print("\nNo path found")

