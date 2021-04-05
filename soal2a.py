# Custom Romania Problem
# Muhammad Rizqi Tsani - 05111940000045
# Greedy Best First Search

import queue
import time
from Node import *

priorityQueue = queue.PriorityQueue()
nodes = Node.init_simplified_romania()

start = nodes['Timisoara']
goal = nodes['Bucharest']

visited = {}

for node in nodes:
  visited[node] = False

start_time = time.time()
priorityQueue.put((start.get_heuristic_value(), start))
total_distance = 0
node = start

while not priorityQueue.empty():
    last_node = node
    node = priorityQueue.get()[1]

    if node != start:
      print(last_node.child[node]['w'])
      total_distance += last_node.child[node]['w']
      last_node = node

    visited[node] = True
    print(node.name)
    if node == goal:
        print("Found goal")
        break
    for child in node.child:
        if child not in visited:
            priorityQueue.put((child.get_heuristic_value(), child))

print(total_distance)
print("--- %s seconds ---" % (time.time() - start_time))