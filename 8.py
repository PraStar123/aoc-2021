import numpy as np

f = open("8.txt", "r")
lines = f.read().splitlines()
digits_data = [line.split('|')[1] for line in lines]
number_data = [i[1:].split(' ') for i in digits_data]
sorted_number_data = []
for data in number_data:
    sorted_row = []
    for el in data:
        sorted_row.append(''.join(sorted(el)))
    sorted_number_data.append(sorted_row)

outputs = np.array(number_data)
# print(outputs)

# def check_if_unique(data):
#     ans = 0
#     for el in data:
#         if(len(el) in [2,3,4,7]):
#             ans += 1
#     return ans

# sum_data = [check_if_unique(x) for x in number_data]
# print(sum(sum_data))

inputs = [line.split('|')[0] for line in lines]
input_data = [i[:-1].split(' ') for i in inputs]
sorted_data = []
for data in input_data:
    sorted_row = []
    for el in data:
        sorted_row.append(''.join(sorted(el)))
    sorted_data.append(sorted_row)
# print("Sorted : ", sorted_data[0])

def find_one(digits):
    for el in digits:
        if len(el) == 2:
            return el

def find_four(digits):
    for el in digits:
        if len(el) == 4:
            return el

def find_seven(digits):
    for el in digits:
        if len(el) == 3:
            return el
            
def find_eight(digits):
    for el in digits:
        if len(el) == 7:
            return el

def find_nine(six_length, four):
    digits = [i for i in four]
    for num in six_length:
        flag = True
        for dig in digits:
            if dig not in num:
                flag = False
                break
        if flag: 
            return num
    

def find_three(five_length, seven):
    digits = [i for i in seven]
    for num in five_length:
        flag = True
        for dig in digits:
            if dig not in num:
                flag = False
                break
        if flag: 
            return num

def find_zero_and_six(six_length, seven):
    digits = [i for i in seven]
    zero = []
    for num in six_length:
        flag = True
        for dig in digits:
            if dig not in num:
                flag = False
                break
        if flag: 
            zero = num
            six_length.remove(zero)
            six = six_length[0]
            return zero,six

def find_two_and_five(five_length, six):
    digits = [i for i in five_length[0]]
    five = []
    for dig in digits:
        if dig not in six:
            return five_length[0],five_length[1]

    return  five_length[1],five_length[0]
    
if __name__ == "__main__":
    total_sum = 0
    for i in range(len(sorted_data)):
        inputs = sorted_data[i]
        five_length = [i for i in inputs if len(i) == 5]
        six_length = [i for i in inputs if len(i) == 6]
        one = find_one(inputs)
        four = find_four(inputs)
        # print(four)
        seven = find_seven(inputs)
        eight = find_eight(inputs)
        nine = find_nine(six_length, four)
        six_length.remove(nine)
        three = find_three(five_length, seven)
        five_length.remove(three)
        zero, six = find_zero_and_six(six_length, seven)
        two, five = find_two_and_five(five_length, six)

        
        dictionary = {
            one: '1',
            two: '2',
            three: '3',
            four: '4',
            five: '5',
            six: '6',
            seven: '7',
            eight: '8',
            nine: '9',
            zero: '0'
        }

        raw_output = sorted_number_data[i]
        output_digits = [dictionary[x] for x in raw_output]
        output = int(''.join(output_digits))
        total_sum += output
    print(total_sum)
