# Problem 1
def find_cruise_length(cruise_lengths, vacation_lengths):
    left, right = 0, len(cruise_lengths) - 1

    while left <= right:
        mid = (left + right) // 2

        if cruise_lengths[mid] == vacation_lengths:
            return True
        elif cruise_lengths[mid] < vacation_lengths:
            left = mid + 1
        else:
            right = mid - 1

    return False

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

# Problem 2
def find_cabin_index(cabins, preferred_deck):

    def binary_search(cabins, left, right, preferred_deck):
        mid = (left + right) // 2

        if left > right:
            return left

        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] < preferred_deck:
            return binary_search(cabins, mid + 1, right, preferred_deck)
        else:
            return binary_search(cabins, left, mid - 1, preferred_deck)
    
    return binary_search(cabins, 0, len(cabins) - 1, preferred_deck)

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))