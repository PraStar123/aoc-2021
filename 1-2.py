f = open("1.txt", "r")
lines = f.read().splitlines()
data = [int(line) for line in lines]

final_data = [(data[i] + data[i-1] + data[i-2]) for i in range(2, len(data))]

ans = [0]
for i in range(1, len(final_data)):
    if final_data[i] - final_data[i-1] > 0 :
        ans.append(1)
    else:
        ans.append(0)
    
# print(ans)
print(sum(ans))
# print(final_data)
print(len(final_data))

