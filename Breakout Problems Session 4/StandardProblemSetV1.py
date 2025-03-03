# Problem 1
def most_endangered(species_list):
    most_endangered_specie = species_list[0]["name"]
    most_endangered_count = species_list[0]["population"]

    for species in species_list:
        if species["population"] < most_endangered_count:
            most_endangered_count = species["population"]
            most_endangered_specie = species["name"]
    return most_endangered_specie

# # Slightly better solution
"""
def most_endangered(species_list):
    most_endangered_specie = species_list[0]
    for specie in species_list[1:]:
        if specie["population"] < most_endangered_specie["population"]:
            most_endangered_specie = specie
    return most_endangered_specie["name"]
"""
species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

# Problem 2
def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species) # ensure that there are unique endangered species
    count = 0
    for species in observed_species:
        if species in endangered_set:
            count += 1
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

# Problem 3
def navigate_research_station(station_layout, observations):
    alphabet_dct = {}
    for i, letter in enumerate(station_layout):
        alphabet_dct[letter] = i
    
    time = 0
    current_station = 0
    for observation in observations:
        time += abs(alphabet_dct[observation] - current_station)
        current_station = alphabet_dct[observation]
    return time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

# Problem 4
def prioritize_observations(observed_species, priority_species):
    priority_set = set(priority_species)
    priority_dct = {}
    non_priority_lst = []

    for species in observed_species:
        if species in priority_set:
            if species in priority_dct:
                priority_dct[species].append(species)
            else:
                priority_dct[species] = [species]
        else:
            non_priority_lst.append(species)

    res = []
    for species in priority_species:
        res.extend(priority_dct[species])

    non_priority_lst.sort()
    res.extend(non_priority_lst)
    
    return res

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

# Problem 5
# O(n^2) solution 
# because there is 4 * O(n) operations inside the while loop and (n/2) iterations which because O(n / (n / 2)) = O(n^2)
# def distinct_averages(species_populations):
#     average_set = set()
#     while species_populations:
#         max_val = max(species_populations)
#         min_val = min(species_populations)
#         average_set.add((max_val + min_val) / 2)
#         species_populations.remove(max_val) # removes the first instance of max_val
#         species_populations.remove(min_val) # removes the first instance of min_val
#     return len(average_set)

# Slightly better solution
# Reason is that we can just do 1 O(n log n) sort instead of O(n) max and min operations each time
# It will become O(1) for min and O(1) for max afterwards.
def distinct_averages(species_populations):
    average_set = set()
    species_populations.sort()

    while species_populations:
        min_val = species_populations.pop(0)
        max_val = species_populations.pop(-1)
        average_set.add((max_val + min_val) / 2)
    return len(average_set)


species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

# Problem 6
def max_species_copies(raised_species, target_species):
    raised_species_dct = {}
    for species in raised_species:
        if species not in raised_species_dct:
            raised_species_dct[species] = 1
        else:
            raised_species_dct[species] += 1

    target_species_dct = {}
    for species in target_species:
        if species not in target_species_dct:
            target_species_dct[species] = 1
        else:
            target_species_dct[species] += 1

    # need to find the min for target_species
    min_species = float("inf")
    for species in set(target_species):
        # this ensures that raised_species will have the species else 0
        min_needed = raised_species_dct.get(species, 0) // target_species_dct[species]
        min_species = min(min_species, min_needed)
    return min_species

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2

# Problem 7
# Trick is to convert the string into an integer to remove leading 0's
def count_unique_species(ecosystem_data):
    unique_species = set()
    curr_species = ""
    for c in ecosystem_data:
        if c.isdigit():
            curr_species += c
        elif curr_species:
            unique_species.add(int(curr_species))
            curr_species = ""

    if curr_species: # so calling an int() on an empty string won't cause an error
        unique_species.add(int(curr_species))
    return len(unique_species)


ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))

# Problem 8
def num_equiv_species_pairs(species_pair):
    for pair in species_pair:
        pair.sort()
    
    species_dct = {}
    for pair in species_pair:
        if tuple(pair) not in species_dct:
            species_dct[tuple(pair)] = 1
        else:
            species_dct[tuple(pair)] += 1
    
    res = 0
    for value in species_dct.values():
        res += value * (value - 1) // 2
    return res

species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))