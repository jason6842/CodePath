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