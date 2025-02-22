def max_audience_performances(audiences):
    dict = {}
    for audience in audiences:
        if audience not in dict:
            dict[audience] = audience
        else:
            dict[audience] += audience
            
    max_value = max(dict.keys())
    return dict[max_value]




audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

# Problem 8 
# O(n^2) time complexity
# def num_popular_pairs(popularity_scores):
#     pair_dict = {}
#     for i in range(len(popularity_scores)):
#         for j in range(i + 1, len(popularity_scores)):
#             if popularity_scores[i] == popularity_scores[j]:
#                 pair = (popularity_scores[i], popularity_scores[j])
#                 if pair not in pair_dict:
#                     pair_dict[pair] = 1
#                 else:
#                     pair_dict[pair] += 1
#     return sum(pair_dict.values())

# O(n) time complexity
def num_popular_pairs(popularity_scores):
    pair_dict = {}
    for score in popularity_scores: # Calculates n, the number of times a score appears in the list
        if score not in pair_dict:
            pair_dict[score] = 1
        else:
            pair_dict[score] += 1
    return (sum((n * (n - 1)) // 2 for n in pair_dict.values())) # Calculates the formula n(n-1)/2 for each score in the list

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 

# Problem 9
def find_stage_arrangement_difference(s, t):
    s_dct = {}
    for i, performer in enumerate(s):
        s_dct[performer] = i

    difference = 0
    for i, performer in enumerate(t):
        difference += abs(i - s_dct[performer])
    return difference

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))

# Problem 10
def num_VIP_guests(vip_passes, guests):
    vip_type_set = set(vip_passes)
    return sum(1 for guest in guests if guest in vip_type_set)
    
vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

# Problem 11
def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre: ## Not the same
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))

# Problem 12
def sort_performers(performer_names, performer_times):
    performance = list(zip(performer_names, performer_times)) # Combines the two lists into a list of tuples
    return [performer[0] for performer in sorted(performance, key=lambda x:x[1], reverse=True)] # Sorts the list of tuples by the second element in the tuple, then returns the first element in the tuple

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))