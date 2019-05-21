from grid import *
import heapq
import time
import numpy as np

open_list = []
close_list = []

def basic_link(grid):
    start = time.time()
    open_list.clear()
    close_list.clear()
    InitializeVertex(grid, grid.start)
    heapq.heappush(open_list, grid.start)
    while len(open_list) > 0:
        s = heapq.heappop(open_list)
        if s == grid.goal:
            end = time.time()
            path = []
            current = s
            while current is not grid.start:
                path.append(current)
                current = current.parent
            path.append(grid.start)
            t = turtle.Turtle()
            grid.draw_grid(t)
            draw_path(path, t, (grid.rows-1)*10)
            print("Time to complete:", end - start)
            return path
        close_list.append(s)
        for t in grid.neighbors_theta(s):
            if t not in close_list:
                if t not in open_list:
                    InitializeVertex(grid, t)
                if grid.lineofsight(s.parent, t):
                    ChoosePath1(grid, s, t)
                else:
                    ChoosePath2(grid, s, t)
    print("No path found")

def InitializeVertex(grid, s):
    if s == grid.start:
        s.parent = s
        s.f = 0
        s.g = 0
    else:
        s.parent = None
        s.f = float("inf")
        s.g = float("inf")

def ChoosePath1(grid, s, t):
    temp_f = s.parent.f + Theta(grid.goal, s.parent, t)
    if temp_f < t.f:
        t.parent = s.parent
        t.f = temp_f
        t.g = temp_f
        if t not in open_list:
            heapq.heappush(open_list, t)
            heapq.heapify(open_list)

def ChoosePath2(grid, s, t):
    temp_f = s.f + Theta(grid.goal, s, t)
    if temp_f < t.f:
        t.parent = s
        t.f = temp_f
        t.g = temp_f
        if t not in open_list:
            heapq.heappush(open_list, t)
            heapq.heapify(open_list)

def Theta(B, A, C):
    if A.x == B.x and A.y == B.y or B.x == C.x and B.y== C.y:
        return 0
    else:
        a = np.array([A.x,A.y])
        b = np.array([B.x,B.y])
        c = np.array([C.x,C.y])
        ba = a-b
        bc = c-b
        return np.arccos((np.dot(ba, bc))/(np.linalg.norm(ba) * np.linalg.norm(bc)))



def UpdateVertex(grid, s, t):
    g_old = t.g
    ComputeCost(grid,s,t)
    if t.g < g_old:
        if t in open_list:
            open_list.remove(t)
            heapq.heapify(open_list)
        heapq.heappush(open_list, t)

def ComputeCost(grid, s, t):
    if grid.lineofsight(s.parent, t):
        if s.parent.g + c(s.parent, t) < t.g:
            t.parent = s.parent
            t.g = s.parent.g + c(s.parent, t)
            t.f = s.parent.f + c(s.parent, t)
    else:
        if s.g + c(s, t) < t.g:
            t.parent = s
