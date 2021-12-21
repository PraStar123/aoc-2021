import pandas as pd 
import numpy as np
import csv

f = open("1.txt", "r")
lines = f.read().splitlines()
data = [int(line) for line in lines]

ans = [0]
for i in range(1, len(data)):
    if data[i] - data[i-1] > 0 :
        ans.append(1)
    else:
        ans.append(0)
    

print(sum(ans))
print(len(data))
