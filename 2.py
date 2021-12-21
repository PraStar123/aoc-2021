f = open("2.txt", "r")
lines = f.read().splitlines()

commands = [line.split() for line in lines]
# print(commands)

dist = 0
depth = 0
for cmd in commands:
    if cmd[0] == 'forward':
        dist += int(cmd[1])
    elif cmd[0] == 'down':
        depth += int(cmd[1])
    elif cmd[0] == 'up':
        depth -= int(cmd[1])

def newInstructions(commands):
    dist = 0
    aim = 0
    depth = 0

    for cmd in commands:
        if cmd[0] == 'forward':
            dist += int(cmd[1])
            depth += (aim*int(cmd[1]))
        elif cmd[0] == 'down':
            aim += int(cmd[1])
        elif cmd[0] == 'up':
            aim -= int(cmd[1])
    
    return [dist, depth]

ans = newInstructions(commands)
print(ans[0]*ans[1])

# print(dist)
# print(depth)
# print(dist*depth)
