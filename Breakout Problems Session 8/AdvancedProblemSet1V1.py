# Problem 1
def count_unique_characters(script):
    # Time Complexity: O(1), operations of dictionary
    # Space Complexity: O(1), operaitons of dictionary
    return len(script)
        

print("----------Problem 1----------")
script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys))

# Problem 2
def find_most_frequent_keywords(scenes):
    # Time Complexity: O(n * m), n is the number of scenes, m is the number of keywords in each scene
    # Space Complexity: O(m), m is the number of unique keywords
    # Worst case: all keywords are unique
    keyword_dct = {}
    for value in scenes.values():
        for keyword in value:
            if keyword not in keyword_dct:
                keyword_dct[keyword] = 1
            else:
                keyword_dct[keyword] += 1
    max_freq = max(keyword_dct.values())
    
    return [key for key, value in keyword_dct.items() if value == max_freq]

print("----------Problem 2----------")
scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes)) 

# Problem 3
from collections import deque
def track_scene_transitions(scenes):
    # Time Complexity: O(n), n is the number of scenes
    # Space Complexity: O(n), n number of scenes from the scenes list
    # Edge cases
    # 1. No scenes
    # 2. Only one scene, so no transition
    if not scenes or len(scenes) < 2:
        return
    
    queue = deque(scenes)
    while len(queue) > 1:
        print(f"Transition from {queue.popleft()} to {queue[0]}")
    
print("----------Problem 3----------")
track_scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution\n"]
track_scene_transitions(track_scenes)

track_scenes1 = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(track_scenes1)