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

# Problem 5
# def find_missing_clues(clues, lower, upper):
#     missing_clues = []
#     for i in range(1, len(clues)):
#         if clues[i - 1] + 1 != clues[i]:
#             missing_clues.append([clues[i - 1] + 1, clues[i] - 1])
#     if clues[-1] != upper:
#         missing_clues.append([clues[-1] + 1, upper])
#     return missing_clues

def find_missing_clues(clues, lower, upper):
    '''
    1. Add a upper + 1 so it performs the checks for every clue
    2. Set a prev variable to lower - 1 to keep track of the previous clue
    3. Iterate through the clues
    4. If the difference between the current clue and the previous clue is greater than 1, there is a missing range
    5. Append the [prev + 1, num - 1] to the missing_ranges list
    6. Update the prev variable to the current clue
    '''
    missing_ranges = []
    clues.append(upper + 1)
    prev = lower - 1
    for num in clues:
        if num - prev > 1: # There's a missing range
            missing_ranges.append([prev + 1, num - 1])
        prev = num
    return missing_ranges

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))

# Problem 6
def harvest(vegetable_patch):
    harvest = 0
    for n in range(len(vegetable_patch)):
        for m in range(len(vegetable_patch[n])):
            if vegetable_patch[n][m] == 'c':
                harvest += 1
    return harvest

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch))

# Problem 7
def good_pairs(pile1, pile2, k):
    good_count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                good_count += 1

    return good_count

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))

# Problem 8
def local_maximums(grid):
    n = len(grid)
    # Create the (n - 2) * (n - 2) grid of local maximums
    local_maxes = [[0] *(n - 2) for _ in range(n - 2)]
    print(local_maxes)
    for i in range(n - 2):
        for j in range(n - 2):
            local_maxes[i][j] = max(grid[i][j], grid[i][j + 1], grid[i][j + 2],
                                    grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                                    grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2])
            print(grid[i][j], grid[i][j + 1], grid[i][j + 2],
                                    grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                                    grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2])
    return local_maxes


grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))
