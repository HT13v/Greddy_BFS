import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

def greedy_bfs(graph, start, goal, heuristic):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, Node(start, heuristic[start]))
    while open_list:
        current_node = heapq.heappop(open_list)
        current_name = current_node.name
        print(f"{current_name}")
        if current_name == goal:
            print(f"Goal {goal} found!")
            return True
        closed_list.add(current_name)
        for neighbor in graph[current_name]:
            if neighbor not in closed_list:
                heapq.heappush(open_list, Node(neighbor, heuristic[neighbor]))
    print(f"Goal {goal} not found.")
    return False
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 7,
    'E': 2,
    'F': 3,
    'G': 1
}

start = 'A'
goal = 'E'
greedy_bfs(graph, start, goal, heuristic)
