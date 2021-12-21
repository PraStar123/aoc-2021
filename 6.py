from collections import Counter
from os import cpu_count

f = open("5.txt", "r")
data = f.read().splitlines()

initial = [int(i) for i in data[0].split(',')]
# print(initial)
count = len(initial)

cnt = Counter(initial)
print("Initial counter : ", cnt)
days = 256
for i in range(days):
    new = 0
    for j in range(9):
        if j == 0:
            new = cnt[0]
            cnt[0] = 0
        else :
            cnt[j-1] += cnt[j]
            cnt[j] = 0
    cnt[6] += new
    cnt[8] += new
    print("After day: ", i+1)
    print(cnt)

print(sum(cnt.values()))

# total = 0
# for j in range(len(initial)):
#     start = []
#     start.append(initial[j])
#     for i in range(256):
#         for k in range(len(start)):
#             new = start[k] - 1
#             if new < 0:
#                 start[k] = 6
#                 start.append(8)
#             else:
#                 start[k] = new
#     total += len(start)
#     print("Completed =====: ", j)
# print("Initial length: ", count)
# print("Final length: ", len(initial))