# def blueprint_approval(blueprints):
    

# Problem 2
# def build_skyscrapers(floors):
#     prev_floor = floors[0]
#     count = 1
#     for i in range(1, len(floors)):
#         if floors[i] < prev_floor:
#             count += 1
#         prev_floor = floors[i]
#     return count

# Stack approach
def build_skyscrapers(floors):
    stack = []
    skyscrapers = 0
    for floor in floors:
        # If there are elements in the stack and the top of the stack is greater than the current floor, pop the top of the stack
        while stack and stack[-1] > floor: 
            stack.pop()

        # If stack is empty or the top of the stack is smaller than the current floor, create a new skyscraper
        if not stack or stack[-1] < floor:
            skyscrapers += 1
            stack.append(floor)

    return skyscrapers


# print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
# print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
# print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

# Problem 3
def max_corridor_area(segments):
    """
    U: 
        1. Each element represents a width.
        2. Distance - right minus left
        3. Area is the minimum width of the two segments multiplied distance between them
    M: Two pointers
    P: Have two pointers, one at the start and one at the end. Calculate the area by finding the min value between the 
        two multiplied by their distance. While doing this keep track of the overall maximum area
    """
    left, right = 0, len(segments) - 1
    max_area = float('-inf')

    while left < right:
        distance = right - left
        if segments[left] < segments[right]:
            min_width = segments[left]
            left += 1
        else:
            min_width = segments[right]
            right -= 1

        curr_area = min_width * distance
        max_area = max(max_area, curr_area)

    return max_area

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 