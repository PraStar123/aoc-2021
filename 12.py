from collections import defaultdict

f = open("12.txt", "r")
lines = f.read().splitlines()
edge_list = defaultdict(list)
for line in lines:
    edge = line.strip().split('-')
    edge_list[edge[0]].append(edge[1])
    edge_list[edge[1]].append(edge[0])

visited = dict()
res = 0
# print(edge_list)
def traversal(edge_list, node):
    global res,visited
    if node.islower() and visited[node] == 2:
        return 
    if node == 'end':
        res += 1
        return

    if node.islower():
        visited.append(node)
    
    for nd in edge_list[node]:
        traversal(edge_list, nd)
        
    if node.islower():
        visited.remove(node)

traversal(edge_list, 'start')
print(res)
