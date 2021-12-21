def get_data():
    pipes = [i for i in open("5.txt", "r").read().splitlines()]
    end_points = [i.split(' -> ') for i in pipes]

    end_points2 = []
    for row in end_points:
        temp = []
        for ep in row:
            temp.append([int(x) for x in ep.split(',')])
        end_points2.append(temp)

    return end_points2
    
def get_data_max(data):
    x_max = 0
    y_max = 0
    for ep in data:
        cxmax = max(ep[0][0], ep[1][0])
        cymax = max(ep[0][1], ep[1][1])
        if cxmax > x_max:
            x_max = cxmax
        if cymax > y_max:
            y_max = cymax
    return (x_max, y_max)

data = get_data()
maxes = get_data_max(data)
print("X max :== ",maxes[0])
print("Y max :== ",maxes[1])

rows = [0 for i in range(maxes[0]+1)]
grid = [rows.copy() for i in range(maxes[1]+1)]

def print_grid(grid):
    for row in grid:
        print(row, "\n")

for ep in data:
    if ep[0][0] == ep[1][0]:
        ymin, ymax = min(ep[0][1],ep[1][1]), max(ep[0][1],ep[1][1])
        # print("ymin ==", ymin, "ymax ==", ymax)
        for y in range(ymin, ymax + 1):
            grid[y][ep[0][0]] += 1
    elif ep[0][1] == ep[1][1]:
        xmin, xmax = min(ep[0][0],ep[1][0]), max(ep[0][0],ep[1][0])
        # print("xmin ==", xmin, "xmax ==", xmax)
        for x in range(xmin, xmax + 1):
            grid[ep[0][1]][x] += 1
    else:
        xstart = ep[0][0]
        xend = ep[1][0]
        ystart = ep[0][1]
        yend = ep[1][1]
        xdiff = (xend - xstart) // abs(xend - xstart)
        ydiff = (yend - ystart) // abs(yend - ystart)
        x = xstart
        y = ystart
        flag = True
        while flag:
            grid[y][x] += 1
            if x == xend or y == yend:
                flag = False 
            x += xdiff
            y += ydiff

    # print_grid(grid)
    # user = input("Input here ...")

print(grid)
total_points = 0
for row in grid:
    for el in row:
        if el > 1:
            total_points += 1

print(total_points)