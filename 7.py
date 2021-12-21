import numpy as np

f = open("7.txt", "r")
lines = f.read().splitlines()
data = [int(x) for x in lines[0].split(',')]
data.sort()
print(len(data))

pos = []
#print(data)
if (len(data) % 2) == 0:
    med_pos = len(data) // 2
    #print(med_pos)
    pos.append(data[med_pos-1])
    pos.append(data[med_pos])
else:
    med_pos = len(data) // 2
    #print(med_pos)
    pos.append(data[med_pos])


if len(pos) == 1:
    median = pos[0]
else:
    median = (pos[0] + pos[1]) // 2 

def find_sum(nums):
    total = 0
    for el in nums:
        total += abs(median - el)
    #print(total)  

# find_sum(data)


def find_sum_from_avg(nums):
    for avg in range(471,476):
        total_l = 0
        for num in nums:
            diff = abs(avg - num)
            total_l += (diff*diff + diff) / 2
        print("total l2: " + str(total_l) + " Avg: " + str(avg))

find_sum_from_avg(data)

def find_avg(nums):
    total_sum = sum(nums)
    avg = total_sum / len(nums)
    print(avg)

# find_avg(data)