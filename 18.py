class SnailfishNumber:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def print_number(self):
        print("Left Number is: ", self.left)
        print("Right Number is: ", self.right)


f = open("18t.txt", "r")
raw_lines = f.read().splitlines()
lines = [raw_lines[0]]
print(lines[0])

stack_list = []
for line in lines:
    stack = []
    for char in line:
        print(char)
        if char == '[' or char == ',':
            continue 
        if char == ']':
            right = stack.pop()
            left = stack.pop()
            sn = SnailfishNumber(left, right)
            stack.append(sn)
            continue
        print("Stack : == ", stack)
        stack.append(char)
    print("Length = ", len(stack))
    stack_list.append(stack[0])

# print(stack_list[0].left)
# print(stack_list[0].right)
# stack_list[0].print_number()

def add_snailfish_numbers(num1, num2):
    return SnailfishNumber(num1, num2)

