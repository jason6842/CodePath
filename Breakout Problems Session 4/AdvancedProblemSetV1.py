# def blueprint_approval(blueprints):
#     ans = []
#     min_val = float('inf')
#     while blueprints:
#         min_val = min(blueprints)
#         if 

"""
You are an architect designing a corridor for a futuristic dream space. The corridor is represented by a list of integer values where each value represents the width of a segment of the corridor. 
Your goal is to find two segments such that the corridor formed between them (including the two segments) has the maximum possible area. 
The area is defined as the minimum width of the two segments multiplied by the distance between them.

You need to return the maximum possible area that can be achieved.

def max_corridor_area(segments):
    pass
Example Usage:

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 
"""

def max_corridor_area(segments):
    left = 0
    right = len(segments) - 1
    max_corridor = float('-inf')

    while left < right:
        distance = right - left
        if segments[left] < segments[right]:
            min_width = segments[left]
            left += 1
        else:
            min_width = segments[right]
            right -= 1

        area = min_width * distance
        max_corridor = max(area, max_corridor)
        

    return max_corridor

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 