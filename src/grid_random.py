from grid import *
import random

f_name = input("Input output name: ")
f = open(f_name, "w")
density = float(input("Input density of obstacles: "))
row = int(input("Input rows:"))
col = int(input("Input cols:"))


corners = []
for i in range(row):
    corners.append([])
    for j in range(col):
        if random.random() < density and 0 < i and 0 < j:
            corners[i].append(1)
            corners[i-1][j] = 1
            corners[i-1][j-1] = 1
            corners[i][j-1] = 1
        else:
            corners[i].append(0)
while(True):
    start_x = random.randint(0,col-1)
    start_y = random.randint(0,row-1)
    if corners[start_y][start_x] == 0:
        break

while(True):
    goal_x = random.randint(0,col-1)
    goal_y = random.randint(0,row-1)
    if corners[goal_y][goal_x] == 0:
        break

grid_random = Grid(row, col, [start_x,start_y],[goal_x,goal_y],corners)
t = turtle.Turtle()
s = t.getscreen()
grid_random.draw_grid(t)
s.exitonclick()
for i in range(row):
    for j in range(col):
        if i == start_y and j == start_x:
            f.write("S ")
        elif i == goal_y and j == goal_x:
            f.write("G ")
        else:
            f.write(str(corners[i][j]) + " ")
    f.write("\n")
f.close()
