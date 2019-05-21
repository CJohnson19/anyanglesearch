from grid import *
import heapq
import time

open_list = []
close_list = []

def lazy_theta(grid):
    start = time.time()
    grid.start.g = 0
    grid.start.parent = grid.start
    open_list.clear()
    close_list.clear()
    heapq.heappush(open_list, grid.start)
    while len(open_list) > 0:
        s = heapq.heappop(open_list)
        SetVertex(grid, s)
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
            print("Time to complete", end - start)
            return path
        close_list.append(s)
        for t in grid.neighbors_theta(s):
            if t not in close_list:
                if t not in open_list:
                    t.g = float("inf")
                    t.f = float("inf")
                    t.parent = None
                UpdateVertex(grid, s, t)
    print("No path found")

def UpdateVertex(grid, s, t):
    g_old = t.g
    ComputeCost(grid,s,t)
    if t.g < g_old:
        if t in open_list:
            open_list.remove(t)
            heapq.heapify(open_list)
        heapq.heappush(open_list, t)

def ComputeCost(grid, s, t):
    if s.parent.g + c(s.parent, t) < t.g:
        t.parent = s.parent
        t.g = s.parent.g + c(s.parent, t)
        t.f = s.parent.f + c(s.parent, t)

def SetVertex(grid, s):
    if not grid.lineofsight(s.parent, s):
        min_parent_cost = float("inf")
        new_parent = None
        for i in grid.neighbors_theta(s):
            if i.g + c(i, s) < min_parent_cost and i in close_list:
                min_parent_cost = i.g + c(i,s)
                new_parent = i
        s.parent = new_parent
        s.g = min_parent_cost
        s.f = min_parent_cost

def test_lazy_theta_medium():
    medium =[\
            [0,0,0,0,0,0],\
            [0,0,0,0,0,0],\
            [0,0,1,1,0,0],\
            [0,0,1,1,0,0],\
            [0,0,0,0,0,0]\
            ]
    grid_medium = Grid(5,6,[0,0],[4,5], medium)
    lazy_theta(grid_medium)
def test_lazy_theta_easy():
    easy = [\
            [0,0,0],\
            [0,0,0],\
            [0,0,0]]
    grid_easy = Grid(3,3,[0,0],[2,2], easy)
    lazy_theta(grid_easy)
def test_lazy_theta_block():
    block = [\
            [0,0,0],\
            [1,1,0],\
            [1,1,0]]
    grid_block = Grid(3,3,[0,0],[2,2], block)
    lazy_theta(grid_block)
def test_lazy_theta_example():
    corners = [\
            [0,1,1,0,0],\
            [0,1,1,1,1],\
            [0,0,0,1,1]\
            ]
    grid_example = Grid(3,5,[0,3],[2,0], corners)
    lazy_theta(grid_example)
