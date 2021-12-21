import numpy as np

f = open("10.txt", "r")
lines = f.read().splitlines()
print(lines[0])

def get_points(x):
    points = {
        ')': 3,
        '}': 1197,
        ']': 57,
        '>': 25137
    }
    return points.get(x, 0)

total_syntax_score = 0

incomplete_lines = []
incomplete_stacks = []

for line in lines:
    stack = []
    syntax_score = 0
    for el in line:
        # print(stack)
        # print(el)
        if el == '{' or el == '[' or el == '(' or el == '<':
            stack.append(el)
        else:
            if el == '}' and stack.pop() != '{':
                syntax_score += get_points(el)
                break
            if el == ')' and stack.pop() != '(':
                syntax_score += get_points(el)
                # print("here")
                break
            if el == ']' and stack.pop() != '[':
                syntax_score += get_points(el)
                break
            if el == '>' and stack.pop() != '<':
                syntax_score += get_points(el)
                break
    if syntax_score == 0:
        incomplete_lines.append(line)
        incomplete_stacks.append(stack)
    total_syntax_score += syntax_score
    

# print(incomplete_lines)
# print(incomplete_stacks)

def stack_autocomplete(incomplete):
    autocomplete = []
    # print("Incomplete: ")
    # print(incomplete)
    for el in incomplete:
        if el == '{':
            print("her")
            autocomplete.append('}')
        if el == '(':
            autocomplete.append(')')
        if el == '<':
            autocomplete.append('>')
        if el == '[':
            autocomplete.append(']')
    return autocomplete[::-1]

autocomplete_stacks = []
for stack in incomplete_stacks:
    autocomplete_stacks.append(stack_autocomplete(stack))

def get_score(x):
    scores = {
        ')': 1,
        '}': 3,
        ']': 2,
        '>': 4
    }
    return scores.get(x, 0)


autocomplete_scores = []
for stack in autocomplete_stacks:
    score = 0
    print("Stack :")
    print(stack)
    for el in stack:
        print("Score now: ")
        print(score)
        score *= 5
        score += get_score(el)
        print("Score later: ")
        print(score)
    autocomplete_scores.append(score)

sorted_scores = sorted(autocomplete_scores)
mid = len(sorted_scores) // 2
print(sorted_scores[mid])
