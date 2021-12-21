# f = open("21t.txt", "r")
# lines = f.read().splitlines()
from collections import Counter
from typing import final

start1 = 5
start2 = 6
print("Player 1 starting pos: ", start1)
print("Player 2 starting pos: ", start2)

rolls = 0
init_roll = 1
rolls_set = [] 
for i in range(3):
    for j in range(3):
        for k in range(3):
            rolls_set.append(i+j+k+3)
rolls_prob = Counter(rolls_set)


def play_turn(curr_roll, curr_pos):
    roll = curr_roll
    pos = curr_pos
    total_roll = 0
    for i in range(3):
        if roll > 100:
            roll -= 100
        total_roll += roll
        roll += 1
    
    pos += (total_roll % 10)
    if pos > 10:
        pos = pos % 10
    return pos, roll

def play_turn_universes(player_dict):
    temp_dict = dict()
    for key in player_dict:
        p_pos, p_score = key
        for roll in rolls_prob:
            final_pos = p_pos + roll
            if final_pos > 10: 
                final_pos %= 10
            final_score = p_score + final_pos
            temp_dict.setdefault((final_pos, final_score), 0)
            temp_dict[(final_pos, final_score)] += rolls_prob[roll] * player_dict[key]
    return temp_dict
    


next_roll = init_roll
next_pos1 = start1
next_pos2 = start2
p1_score = 0 
p2_score = 0
print("\nAnswer part 1 ==>")
print("--------------------------")
while True:
    next_pos1, next_roll = play_turn(next_roll, next_pos1)
    rolls += 3
    p1_score += next_pos1
    if p1_score >= 1000:
        print("Player 1 score:", p1_score)
        print("Player 2 score:", p2_score)
        print("Rolls: ", rolls)
        print("Answer: ", p2_score*rolls)
        break

    
    next_pos2, next_roll = play_turn(next_roll, next_pos2)
    rolls += 3
    p2_score += next_pos2
    if p2_score >= 1000:
        print("Player 1 score:", p1_score)
        print("Player 2 score:", p2_score)
        print("Rolls: ", rolls)
        print("Answer: ", p1_score*rolls)
        break



p1_universes = 0
p2_universes = 0
p1_dict = dict()
p1_dict[(start1,0)] = 1
p2_dict = dict()
p2_dict[(start2,0)] = 1
while True:
    p1_dict = play_turn_universes(p1_dict)
    rolls += 3
    p1_remove = []
    for key in p1_dict:
        if key[1] >= 21:
            p1_universes += (p1_dict[key]*sum(p2_dict.values()))
            p1_remove.append(key)
    for key in p1_remove:
        del p1_dict[key]
    # print("Player 1 dict: ", p1_dict)
    # input()

    p2_dict = play_turn_universes(p2_dict)
    rolls += 3
    p2_remove = []
    for key in p2_dict:
        if key[1] >= 21:
            p2_universes += (p2_dict[key]*sum(p1_dict.values()))
            p2_remove.append(key)
    for key in p2_remove:
        del p2_dict[key]
    # print("Player 2 dict: ", p2_dict)
    # input()

    if len(p1_dict) == 0 and len(p2_dict) == 0:
        break
print("\nAnswer part 2 ==>")
print("--------------------------")
print("Quantum die outcome distribution:", rolls_prob, "len :", len(rolls_set))
print("Player 1 universes: == ", p1_universes)
print("Player 2 universes: == ", p2_universes)
print("Answer: ", max(p1_universes, p2_universes))