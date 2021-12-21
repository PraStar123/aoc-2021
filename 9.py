import numpy as np

f = open("9.txt", "r")
lines = f.read().splitlines()
width = len(lines[0])
height = len(lines)


grid = []
for i in range(height):
    line = []
    for j in range(width):
        line.append(int(lines[i][j]))
    grid.append(line)

def check_sides(data, h, w, i, j):
    try:
        if (i < 0 or data[i-1][j] > data[i][j]):
            if (i > h-2 or data[i+1][j] > data[i][j]):
                if (j < 0 or data[i][j-1] > data[i][j]):
                    if (j > w-2 or data[i][j+1] > data[i][j]):
                        return True
    except:
        print("I: " + str(i))
        print("J: " + str(j))
        print("H: " + str(h))
        print("W: " + str(w))
    return False

total = 0
low_points = []
for i in range(height):
    for j in range(width):
        if (check_sides(grid, height, width, i, j)):
            total += 1
            total += int(grid[i][j])
            low_points.append((i,j))

print("Answer part 1: ", total)
visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

def get_basins(grid, low_points):
    basins = []
    for pt in low_points:
        i,j = pt
        basin_size = find_paths(i,j,grid,visited)
        basins.append(basin_size)
    return basins

imax = len(grid)
jmax = len(grid[0]) 
def find_paths(i, j, grid, visited):
    if i < 0 or j < 0 or i >= imax or j >= jmax or (grid[i][j] == 9) or visited[i][j]:
        return 0
    visited[i][j] = True
    total = find_paths(i+1, j, grid, visited)
    total += find_paths(i, j+1, grid, visited)
    total += find_paths(i-1,j, grid, visited)
    total += find_paths(i, j-1, grid, visited)
    return total + 1  

basins = get_basins(grid, low_points)
print("Top three Basins = ", sorted(basins, reverse=True)[:3])
sorted_basins = sorted(basins, reverse=True)
print("Answer part 2: ", sorted_basins[0]*sorted_basins[1]*sorted_basins[2])
