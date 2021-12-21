import numpy as np

f = open("3.txt", "r")
data = f.read().splitlines()
# data = [line.split() for line in lines]

def calcGammaAndEpsilon(data):
  freq_0 = [0 for i in range(len(data[0]))]
  freq_1 = [0 for i in range(len(data[0]))]
  
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data[i][j] == '0':
        freq_0[j] += 1
      else :
        freq_1[j] += 1
  
  diff = np.subtract(freq_0, freq_1)
  gamma_rate = (diff < 0).astype(int)
  epsilon_rate = (diff > 0).astype(int)
  print(gamma_rate)
  print(epsilon_rate)
  return [gamma_rate, epsilon_rate]

def calcO2(initial_data):
  data = initial_data
  col = 0
  while len(data) > 1 :
    list_0 = []
    list_1 = []
    for i in range(len(data)) :
      if (data[i][col]) == '0':
        list_0.append(data[i])
      else:
        list_1.append(data[i])

    if len(list_1) >= len(list_0):
      data = list_1
    else:
      data = list_0

    col += 1

  return data

def calcCO2(initial_data):
  data = initial_data
  col = 0
  while len(data) > 1 :
    list_0 = []
    list_1 = []
    for i in range(len(data)) :
      if (data[i][col]) == '0':
        list_0.append(data[i])
      else:
        list_1.append(data[i])

    if len(list_1) < len(list_0):
      data = list_1
    else:
      data = list_0

    col += 1

  return data  



## Puzzle 1
# puz1(data)
# Gamma rate = 1143
# Epsilon rate = 2952


## Puzzle 2
# o2_generator = calcO2(data)
# print(o2_generator)
# co2_scrubber = calcCO2(data)
# print(co2_scrubber)
# O2 Generator = 1909
# Co2 Scrubber = 2322 