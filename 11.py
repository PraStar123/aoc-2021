f = open("11.txt", "r")
lines = f.read().splitlines()
grid = []
for row in lines:
    formatted_row = [int(x) for x in row]
    grid.append(formatted_row)

height = len(grid)
width = len(grid[0])
def change_energy(grid, flash, i, j):
    if i < 0 or j < 0 or i >= height or j >= width or flash[i][j] == 1: 
        return
    
    grid[i][j] += 1
    if grid[i][j] > 9:
        grid[i][j] = 0
        flash[i][j] = 1
        change_energy(grid, flash, i+1, j)
        change_energy(grid, flash, i+1, j-1)
        change_energy(grid, flash, i+1, j+1)
        change_energy(grid, flash, i, j+1)
        change_energy(grid, flash, i, j-1)
        change_energy(grid, flash, i-1, j-1)
        change_energy(grid, flash, i-1, j)
        change_energy(grid, flash, i-1, j+1)


def count_flashes(flash_grid):
    total = 0
    for row in flash_grid:
        total += sum(row)
    return total

def print_grid():
    for row in grid:
        print(row)

def move_steps(grid, steps):
    total_flashes = 0
    tot_octos = width * height
    for n in range(steps):
        flash = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                change_energy(grid, flash, i, j)
        flashes_this_step = count_flashes(flash) 
        total_flashes += flashes_this_step
        # if n in [0,1,2,3,4,5,6,7,8,9,19,29,39,49,59,69,79,89,99]:
        if flashes_this_step == tot_octos :
            print_grid()
            print("Flashes in step",n+1, " :", flashes_this_step)
            print("Total flashes till now: ", total_flashes)
            input()
    return total_flashes

ans = move_steps(grid, 500)
print("Ans to part 1: ==", ans)