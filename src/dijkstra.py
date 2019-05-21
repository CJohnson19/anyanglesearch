from grid import *
import heapq
import time

def dijkstra(graph):
    start = time.time()
    unvisited_nodes = [y for x in graph.grid for y in x]
    for i in unvisited_nodes:
        i.f = float("inf")
    graph.goal.f = 0
    heapq.heapify(unvisited_nodes)
    while(len(unvisited_nodes) > 0):
        cur_node = heapq.heappop(unvisited_nodes)
        heapq.heapify(unvisited_nodes)
        for node in graph.neighbors_a(cur_node):
            d = cur_node.f + c(cur_node, node)
            if d < node.f:
                node.f = d
                node.parent = cur_node
                heapq.heapify(unvisited_nodes)
        cur_node.visted = True
        if cur_node == graph.start:
            break
    # cur_node is now graph.goal
    end = time.time()
    path = []
    current = cur_node
    while current is not None:
        path.append(current)
        current = current.parent
    t = turtle.Turtle()
    graph.draw_grid(t)
    draw_path(path, t, (graph.rows-1) * 10)
    print("Time to complete:", end - start)
    return path

