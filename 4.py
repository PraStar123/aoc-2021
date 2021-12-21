from typing import Counter
import numpy as np

f = open("4.txt", "r")
lines = f.read().splitlines()
print(lines[0])
raw_numbers = lines[0]
numbers = [i for i in raw_numbers.split(',')]
print(len(numbers))
for el in numbers:
    print(el)
list_of_tickets = []

ticket = []
for i in range(2, len(lines)):
    if (len(lines[i]) == 0):
        list_of_tickets.append(ticket)
        ticket = []
        continue
    else :
        ticket.append(lines[i])
list_of_tickets.append(ticket)


def get_min_moves(tk, numbers):
    i_list = [0 for i in range(5)]
    j_list = [0 for i in range(5)]
    moves = 0
    diff = 0
    for num in numbers:
        for i in range(5):
            raw_cells = tk[i].split(' ')
            cells = [i for i in raw_cells if i.strip()]
            for j in range(5):
                if cells[j] == num:
                    i_list[i] += 1
                    j_list[j] += 1
                    print(num)
                    diff += int(num)
                    moves += 1
                    if (i_list[i] == 5 or j_list[j] == 5):
                        return  [moves, diff, num]
        moves += 1


low_ticket = []
low_count = 0
low_diff = 0
low_num = 1
for tk in list_of_tickets:
    result = get_min_moves(tk, numbers)
    count = result[0]
    diff = result[1]
    that_num = result[2]
    if (count > low_count):
        low_count = count
        low_ticket = tk 
        low_diff = diff
        low_num = that_num

sum_total = 0
print(low_ticket) 
for row in low_ticket:
    raw_cells = [i for i in row.strip().split(' ')]
    cells = [int(i) for i in raw_cells if i.strip()]
    # print(int(cells[1]))
    sum_total += sum(cells)
print("TOtal: ===")
print(sum_total)
print("Low num : ---")
print(low_num)
final_result = sum_total - low_diff
print("Final Result : ---")
print(final_result * int(low_num))