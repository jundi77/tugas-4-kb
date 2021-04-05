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

while not priorityQueue.empty():
    node = priorityQueue.get()[1]
    visited[node] = True
    print(node.name)
    if node == goal:
        print("Found goal")
        break
    for child in node.child:
        if child not in visited:
            priorityQueue.put((child.get_heuristic_value(), child))
print("--- %s seconds ---" % (time.time() - start_time))