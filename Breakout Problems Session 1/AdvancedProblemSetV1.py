# Problem 1 
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))

# Problem 2
def final_value_after_operations(operations):
    tigger = 1
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            tigger += 1
        elif operation =="trouncy" or operation == "pouncy":
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# Problem 3
def tiggerfy(word):
    word_lower = word.lower()
    res = ""
    i = 0
    while i < len(word):
        if i < len(word) - 1 and word_lower[i:i + 2] == "gg":
            i += 2
        elif i < len(word) - 1 and word_lower[i:i + 2] == "er":
            i += 2
        elif word_lower[i] in "ti":
            i += 1
        else:
            res += word[i]
            i += 1
    return res


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))

# Problem 4
def non_decreasing(nums):
    isModify = False
    for i in range (len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if isModify == True:
                return False
            isModify = True
    return True
        
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))