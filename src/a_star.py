from grid import *
import heapq
import time

open_list = []
close_list = []

def a_star(grid):
    start = time.time()
    grid.start.g = 0
    grid.start.parent = None
    open_list.clear()
    close_list.clear()
    heapq.heappush(open_list, grid.start)
    while len(open_list) > 0:
        s = heapq.heappop(open_list)
        if s == grid.goal:
            end = time.time()
            path = []
            current = s
            while current is not None:
                path.append(current)
                current = current.parent
            t = turtle.Turtle()
            grid.draw_grid(t)
            draw_path(path, t, (grid.rows-1)*10)
            print("Time to complete:", end - start)
            return path
        close_list.append(s)
        for t in grid.neighbors_a(s):
            if t not in close_list:
                if t not in open_list:
                    t.g = float("inf")
                    t.f = float("inf")
                    t.parent = None
                UpdateVertex(grid, s, t)
    print("No path found")

def UpdateVertex(grid, s, t):
    if s.g + c(s, t) < t.g:
        t.g = s.g + c(s, t)
        t.f = t.g + c(s, t)
        t.parent = s
        if t in open_list:
            open_list.remove(t)
            heapq.heapify(open_list)
        heapq.heappush(open_list, t)

def test_a_star_easy():
    easy = [\
            [0,0,0],\
            [0,0,0],\
            [0,0,0]]
    grid_easy = Grid(3,3,[0,0],[2,2], easy)
    print(a_star(grid_easy))
def test_a_star_block():
    block = [\
            [0,0,0],\
            [1,1,0],\
            [1,1,0]]
    grid_block = Grid(3,3,[0,0],[2,2], block)
    print(a_star(grid_block))
def test_a_star_medium():
    medium =[\
            [0,0,0,0,0,0],\
            [0,0,0,0,0,0],\
            [0,0,1,1,0,0],\
            [0,0,1,1,0,0],\
            [0,0,0,0,0,0]\
            ]
    grid_medium = Grid(5,6,[0,0],[4,5], medium)
    a_star(grid_medium)
def test_a_star_example():
    corners = [\
            [0,1,1,0,0],\
            [0,1,1,1,1],\
            [0,0,0,1,1]\
            ]
    grid_example = Grid(3,5,[0,3],[2,0], corners)
    a_star(grid_example)
