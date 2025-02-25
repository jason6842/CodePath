# Problem 1
def total_treasures(treasure_map):
    return sum(treasure_map.values())

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 

# Problem 2
def can_trust_message(message):
    message = message.replace(" ", "")
    return len(set(message)) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

# Problem 3
def find_duplicate_chests(chests):
    chest_dct = {}
    for chest in chests:
        if chest not in chest_dct:
            chest_dct[chest] = 1
        else:
            chest_dct[chest] += 1
    return [chest for chest in chest_dct if chest_dct[chest] == 2]

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

# Problem 4
def is_balanced(code):
    char_dct = {}
    for c in code:
        if c not in char_dct:
            char_dct[c] = 1
        else:
            char_dct[c] += 1
    max_count = max(char_dct.values())
    isChanged = False
    for key, value in char_dct.items():
        if value == max_count and isChanged == False:
            char_dct[key] -= 1
            isChanged = True
    
            
    return len(set(char_dct.values())) == 1
    

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

# Problem 5
def find_treasure_indices(gold_amounts, target):
    treasure_dct = {}
    for i, gold in enumerate(gold_amounts):
        difference = target - gold
        if difference in treasure_dct:
            return [treasure_dct[difference], i]
        else:
            treasure_dct[gold] = i
    
gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

# Problem 6
# def organize_pirate_crew(group_sizes):
#     pirate_dct = {}
#     res = []
#     for i, pirate in enumerate(group_sizes):
#         if pirate not in pirate_dct:
#             pirate_dct[pirate] = [i]
#         else:
#             if len(pirate_dct[pirate]) < pirate:
#                 pirate_dct[pirate].append(i)
#             else:
#                 res.append(pirate_dct[pirate])
#                 pirate_dct[pirate] = [i]

#     res += list(pirate_dct.values())
#     return res

# only add COMPLETED groups to the result
def organize_pirate_crew(group_sizes):
    pirate_dct = {}
    res = []
    for i, pirate in enumerate(group_sizes):
        if pirate not in pirate_dct:
            pirate_dct[pirate] = []
            
        pirate_dct[pirate].append(i)

        if len(pirate_dct[pirate]) == pirate:
            res.append(pirate_dct[pirate])
            pirate_dct[pirate] = []

    return res
        
group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 

# Problem 7
# def min_steps_to_match_maps(map1, map2):
#     dct1 = {}
#     for c in map1:
#         if c not in dct1:
#             dct1[c] = 1
#         else:
#             dct1[c] += 1

#     for c in map2:
#         if c in dct1:
#             dct1[c] -= 1
#             if dct1[c] == 0:
#                 del dct1[c]

#     return sum(dct1.values())


# An alternative solution is get a frequency map on both map1 and map2, then calculate the fewer occurrence in map 2
def min_steps_to_match_maps(map1, map2):
    dct1 = {}
    dct2 = {}
    for c in map1:
        if c not in dct1:
            dct1[c] = 1
        else:
            dct1[c] += 1

    for c in map2:
        if c not in dct2:
            dct2[c] = 1
        else:
            dct2[c] += 1

    res = 0
    for c in dct1:
        if c in dct2:
            if dct1[c] > dct2[c]:
                res += dct1[c] - dct2[c]
        else:
            res += dct1[c]
    return res



map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))

# Problem 8
def counting_pirates_action_minutes(logs, k):
    