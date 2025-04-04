# Problem 1
def recursive_check_stock(inventory, part_id):

    left = 0
    right = len(inventory) - 1
    
    def binary_search(inventory, left, right, part_id):
        if left > right:
            return False
        mid = (left + right) // 2
        if inventory[mid] == part_id:
            return True
        if inventory[mid] > part_id:
            return binary_search(inventory, left, mid - 1, part_id)
        else:
            return binary_search(inventory, mid + 1, right, part_id)
    
    return binary_search(inventory, left, right, part_id)

print(recursive_check_stock([1, 2, 5, 12, 20], 20))
print(recursive_check_stock([1, 2, 5, 12, 20], 100))

def iterative_check_stock(inventory, part_id):
    left = 0
    right = len(inventory) - 1

    while left <= right:
        mid = (left + right) // 2

        if inventory[mid] == part_id:
            return True 

        if inventory[mid] > part_id:
            right = mid-1
        else:
            left = mid+1

    return False
        
    
print(iterative_check_stock([1, 2, 5, 20, 12], 20))
print(iterative_check_stock([1, 2, 5, 20, 12], 100))

# Problem 3
def find_frequency_positions(transmissions, target_code):
    def find_first_occurrence(arr, target):
        low, high = 0, len(arr) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1  # keep looking on the left
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def find_last_occurrence(arr, target):
        low, high = 0, len(arr) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1  # keep looking on the right
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last
    
    first_index = find_first_occurrence(transmissions, target_code)
    last_index = find_last_occurrence(transmissions, target_code)

    return (first_index, last_index)

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))

def next_greatest_letter(letters, target):
    if letters[-1] < target:
        return letters[0]

    left, right = 0, len(letters) - 1
    last = -1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] == target:
            last = mid
            left = mid + 1
        elif letters[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # print(letters[left], letters[right])

    if letters[left] < target:
        return letters[right]
    else:
        return letters[left]


letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))