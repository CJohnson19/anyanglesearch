from grid import *
import heapq
import time

def ucs(graph):
    start = time.time()
    node = graph.start
    cost = 0
    frontier = [(0,node,[node])]
    explored = []
    while(True):
        cost, node, path = heapq.heappop(frontier)
        if node not in explored:
            explored.append(node)
            if node == graph.goal:
                end = time.time()
                t = turtle.Turtle()
                graph.draw_grid(t)
                draw_path(path, t, (graph.rows-1) * 10)
                print("Time to complete:", end - start)
                return
            for i in graph.neighbors_a(node):
                if i not in explored:
                    total_cost = cost + c(node, i)
                    heapq.heappush(frontier, (total_cost, i, path+[i]))
