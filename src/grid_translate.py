from grid import *
from lazy_theta import *
from theta import *
from a_star import *
from dijkstra import *
from ucs import *
from basic_link import *

f_name = input("Input the file name: ")
f = open(f_name, "r")
corners = []
start_pos = [0,0]
goal_pos = [0,0]
line_no = 0
for line in f:
    cur_line = line.split()
    for i in range(len(cur_line)):
        if cur_line[i] == 'S':
            start_pos = [line_no, i]
            cur_line[i] = 0
        elif cur_line[i] == 'G':
            goal_pos = [line_no, i]
            cur_line[i] = 0
        else:
            cur_line[i] = int(cur_line[i])
    line_no += 1
    corners += [cur_line]
grid_read = Grid(len(corners), len(corners[0]), goal_pos, start_pos, corners)
f.close()
print("Grid dimensions: ", len(corners), "x", len(corners[0]))
print("Goal is:", goal_pos[0], ",", goal_pos[1])
print("Start is:", start_pos[0], ",", start_pos[1])
print("Algorithms available:")
print("\t(L)azy Theta")
print("\t(T)heta")
print("\t(A)-Star")
print("\t(D)ijkstra")
print("\t(U)niform Cost Search")
print("\t(B)asic Link")
while(True):
    choice = input("Input algorithm to run on grid: ").lower()
    if choice == 'l':
        lazy_theta(grid_read)
        break
    elif choice == 't':
        theta(grid_read)
        break
    elif choice == 'a':
        a_star(grid_read)
        break
    elif choice == 'd':
        dijkstra(grid_read)
        break
    elif choice == 'u':
        ucs(grid_read)
        break
    elif choice == 'b':
        basic_link(grid_read)
        break
    else:
        print("Invalid choice")
