from collections import defaultdict, deque
from sys import stdin

def build_graph(n, item_to_index, bad_combos):
    graph = defaultdict(list)
    for bad in bad_combos:
        a = item_to_index[bad[0]]
        b = item_to_index[bad[1]]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def visualize_graph(graph):
    for node, neighbors in graph.items():
        if neighbors:
            neighbors_str = ', '.join(map(str, neighbors))
            print(f"Node {node} is connected to: {neighbors_str}")
        else:
            print(f"Node {node} is not connected to any other nodes.")

def is_bipartite(graph, n, items):
    colors = [-1] * n
    
    for start in range(n):
        if colors[start] == -1:  # Unvisited node
            # Use a queue for BFS
            queue = deque([start])
            colors[start] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:  # If unvisited, color it with the opposite color
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:  # If the same color, it's not bipartite
                        return False, []
    
    walter = [items[i] for i in range(n) if colors[i] == 0]
    jesse = [items[i] for i in range(n) if colors[i] == 1]

    return True, (walter, jesse)


data = []
for line in stdin:
    data.append(line.strip())

n = int(data[0])
items = data[1:n+1]

m = int(data[n+1])
bad_combos = [tuple(data[i].split()) for i in range(n+2, n+2+m)]

item_to_index = {item: idx for idx, item in enumerate(items)}

graph = build_graph(n, item_to_index, bad_combos)
#visualize_graph(graph)

valid, groups = is_bipartite(graph, n, items)
if valid:
    walter, jesse = groups
    print(' '.join(walter))
    print(' '.join(jesse))
else:
    print("impossible")
