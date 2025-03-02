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