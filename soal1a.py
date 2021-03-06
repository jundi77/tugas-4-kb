# Custom Romania Problem
# Muhammad Rizqi Tsani - 05111940000045
# BFS

from collections import deque
import time
from Node import *

def bfs(start, goal):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = cur_node.child
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return visited

nodes = Node.init_simplified_romania()

start = nodes['Timisoara']
goal = nodes['Bucharest']

start_time = time.perf_counter_ns()
visited = bfs(start, goal)
end_time = time.perf_counter_ns()

cur_node = goal
total_distance = 0

print(f'{goal.name} ', end='')

while cur_node != start:
  total_distance += cur_node.child[visited[cur_node]]['w']
  cur_node = visited[cur_node]
  print(f'---> {cur_node.name} ', end='')

print("\nTotal Jarak\t %s" % total_distance)
print("Waktu Eksekusi\t %s ns" % (end_time - start_time))