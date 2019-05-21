import math
import turtle
# We define our grid as 0,0 being in the top left and increasing
# as we reach the bottom right

class Grid:
    def __init__(self, rows, cols, goalIndex, startIndex, corners):
        # takes number of rows and number of columns
        # the index of the start in a list [row,col]
        # the index of the goal in a lit [row, col]
        # a 2 dimensional list of obstacles. 0 or 1, 1 indicates not
        # passable

        # make a list of vertices for the amount of rows and columns
        self.rows = rows
        self.cols = cols
        # Vertexes on the corners of each block
        self.grid = [[Vertex(x, y) for x in range(cols)] for y in range(rows)]
        # List of blocked blocks
        self.obs = [[False for i in range(cols)] for j in range(rows)]

        # set the obstacles to be non-passable
        for i in range(len(corners)):
            for j in range(len(corners[i])):
                if corners[i][j] == 1:
                    self.grid[i][j].passable = False
                    # we check bottom right corner for a blocked cell
                    # not a blocked corner
                    if 0 <= i-1:
                        # if the left side is in the range
                        if 0 <= j-1:
                            # if the top is in the range
                            if corners[i-1][j] == 1 and \
                            corners[i-1][j-1] == 1 and \
                            corners[i][j-1] == 1 and \
                            corners[i][j] == 1:
                                # if all for corners are not passable
                                self.obs[i-1][j-1] = True
                                # update the obstacle list
        #set the start state
        self.start = self.grid[startIndex[0]][startIndex[1]]
        self.start.start = True
        # set the goal state
        self.goal = self.grid[goalIndex[0]][goalIndex[1]]
        self.goal.goal = True


    def lineofsight(self, s, t):
        x0 = s.x
        y0 = s.y
        x1 = t.x
        y1 = t.y
        dy = y1 - y0
        dx = x1 - x0
        f = 0
        if dy < 0:
            dy = -dy
            sy = -1
        else:
            sy = 1
        if dx < 0:
            dx = -dx
            sx = -1
        else:
            sx = 1
        if dx >= dy:
            while x0 != x1:
                f = f + dy
                if f >= dx:
                    if self.obs[y0+((sy-1)//2)][x0+((sx-1)//2)]:
                        return False
                    y0 += sy
                    f -= dx
                if f != 0 and self.obs[y0 + ((sy-1)//2)][x0 + ((sx-1)//2)]:
                    return False
                if dy == 0 and self.obs[y0][x0 + ((sx-1)//2)] and self.obs[y0-1][x0+((sx-1)//2)]:
                    return False
                x0 += sx
        else:
            while y0 != y1:
                f += dx
                if f >= dy:
                    if self.obs[y0+((sy-1)//2)][x0+((sx-1)//2)]:
                        return False
                    x0 += sx
                    f -= dy
                if f != 0 and self.obs[y0+((sy-1)//2)][x0+((sx-1)//2)]:
                    return False
                if dx == 0 and self.obs[y0+((sy-1)//2)][x0] and self.obs[y0+((sy-1)//2)][x0-1]:
                    return False
                y0 += sy
        return True

    def neighbors_a(self, n):
        x = n.x
        y = n.y
        n1 = self.grid[y][x]
        neighbors = []
        for i in range(-1, 2):
            if(0 <= x+i < self.cols):
                for j in range(-1, 2):
                    if(0 <= y+j < self.rows):
                        n2 = self.grid[y+j][x+i]
                        if(i != 0 or j != 0):
                            if self.lineofsight(n1,n2):
                                neighbors.append(n2)
        return neighbors
    def neighbors_theta(self, n):
        x = n.x
        y = n.y
        n1 = self.grid[y][x]
        neighbors = []
        for i in range(-1, 2):
            if(0 <= x+i < self.cols):
                for j in range(-1, 2):
                    if(0 <= y+j < self.rows):
                        n2 = self.grid[y+j][x+i]
                        if(i != 0 or j != 0):
                            if self.lineofsight(n1, n2):
                                neighbors.append(n2)
        return neighbors
    def h(self, n):
        return math.sqrt((self.goal.x - n.x)**2 + (self.goal.y - n.y)**2)

    def print_grid(self):
        for row in self.grid:
            for vertex in row:
                print(vertex, end = ' ')
            print()

    def draw_grid(self, t):
        s = t.getscreen()
        t.speed(0)
        s.delay(0)
        s.tracer(0,0)
        height = (self.rows-1) * 10
        width = (self.cols-1) * 10
        row_step = 10
        height_step = 10
        s.setworldcoordinates(0, 0, width, height);
        # draw the actual blocked or unblocked cells
        for row in range(len(self.obs)):
            for col in range(len(self.obs[row])):
                t.penup()
                t.goto(col*10, height-row*10) # top left
                t.pendown()
                if(self.obs[row][col]):
                    t.color("black", "black")
                else:
                    t.color("black", "white")
                t.begin_fill()
                t.goto(col*10, height-row*10-10) # bottom left
                t.goto(col*10+10, height-row*10-10) # bottom right
                t.goto(col*10+10, height-row*10) # top right
                t.goto(col*10, height-row*10) # top left
                t.end_fill()
                #t.goto(col*10+10, height-row*10-10) # bottom right
                #t.goto(col*10, height-row*10-10) # bottom left
                #t.goto(col*10+10, height-row*10) # top right

        # draw the corners of blocked or unblocked cells
        for row in self.grid:
            for vertex in row:
                t.penup()
                t.goto(vertex.x*10, height-vertex.y*10)
                t.pendown()
                if(vertex.start):
                    t.dot(10,"blue")
                elif(vertex.goal):
                    t.dot(10,"green")
                elif(vertex.passable):
                    t.dot(10,"white")
                else:
                    t.dot(10,"black")
        s.update()


class Vertex:
    def __init__(self, x, y, passable = True, goal=False, start=False):
        self.x = x
        self.y = y
        self.passable = passable
        self.goal = goal
        self.start = start
        self.g = 0
        self.parent = None
        self.f = 0

        # FOR DIJKSTRA
        self.visited = False

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.passable:
            return "(O," + str(self.x) + ", " + str(self.y) + ")"
        else:
            return "(X," + str(self.x) + ", " + str(self.y) + ")"

def draw_path(path,t,height):
    path_length = 0
    t.penup()
    s = t.getscreen()
    t.goto(path[0].x*10, height-path[0].y*10)
    t.pendown()
    t.color('red')
    prev_x = path[0].x*10
    prev_y = height-path[0].y*10
    for i in path:
        x = i.x*10
        y = height-i.y*10
        t.goto(x, y)
        path_length += (((prev_x - x)**2)+ ((prev_y - y)**2)) ** .5
        prev_x = x
        prev_y = y
    s.update()
    print("Path length:", path_length)
    s.exitonclick()


def c(n0, n1):
    return math.sqrt((n0.x - n1.x)**2 + (n0.y - n1.y)**2)

def test_vertex():
    v00 = Vertex(0,0)
    v01 = Vertex(0,1)
    v10 = Vertex(1,0)
    v11 = Vertex(1,1)
    v11.goal = True
    assert v00.x == 0 and v00.y == 0
    assert v01.x == 0 and v01.y == 1
    assert v10.x == 1 and v10.y == 0
    assert v11.x == 1 and v11.y == 1
    assert v00.passable == True
    assert v11.goal == True

def test_print():
    large = \
            [[1,1,1,1,1,1,1,1,1,1],\
            [1,0,0,0,0,0,0,0,0,1],\
            [1,1,0,1,1,1,0,0,0,1],\
            [1,1,0,1,1,0,0,0,0,1],\
            [1,1,0,1,1,1,0,0,0,1],\
            [1,1,0,0,0,0,0,0,0,1],\
            [1,1,1,1,1,1,1,1,1,1]]
    grid_large = Grid(len(large),len(large[0]),[1,1],[3,5], large)
    grid_large.print_grid()

def test_draw():
    large = \
            [[1,1,1,1,1,1,1,1,1,1],\
            [1,0,0,0,0,0,0,0,0,1],\
            [1,1,0,1,1,1,0,0,0,1],\
            [1,1,0,1,1,0,0,0,0,1],\
            [1,1,0,1,1,1,0,0,0,1],\
            [1,1,0,0,0,0,0,0,0,1],\
            [1,1,1,1,1,1,1,1,1,1]]
    grid_easy = Grid(len(large),len(large[0]),[1,1],[5,8], large)
    t = turtle.Turtle()
    grid_easy.draw_grid(t)


def test_grid():
    easy = \
            [[0,0,0],\
            [0,1,0],\
            [0,0,0]]
    grid_easy = Grid(3,3,[0,0],[2,2], easy)
    assert grid_easy.lineofsight(grid_easy.grid[0][0],grid_easy.grid[2][2]) == False
    assert grid_easy.lineofsight(grid_easy.grid[0][0],grid_easy.grid[2][0])
    assert grid_easy.lineofsight(grid_easy.grid[0][0],grid_easy.grid[0][2])
