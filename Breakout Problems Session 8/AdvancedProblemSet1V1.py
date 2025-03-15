# Problem 1
def filter_sustainable_brands(brands, criterion):
    # Time Complexity: O(n), where n is the number of brands
    # Space Complexity: O(m), where m is the number of brands that meet the criterion
    brandList = []
    for brand in brands:
        if criterion in brand["criteria"]:
            brandList.append(brand["name"])
    return brandList

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))

# Problem 2
def count_material_usage(brands):
    # Time Complexity: O(n * m), where n is the number of brands and m is the number of materials in each brand
    # Space Complexity: O(m), where m is the number of unique materials
    material_freq_dct = {}
    for brand in brands:
        for material in brand["materials"]:
            if material not in material_freq_dct:
                material_freq_dct[material] = 1
            else:
                material_freq_dct[material] += 1
    return material_freq_dct

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))

# Problem 3
def find_trending_materials(brands):
    # Time Complexity: O(n * m), where n is the number of brands and m is the number of materials in each brand
    # Space Complexity: O(n * m), where there is m materials for n brands
    unique_trending_materials = set()
    trending_materials_lst = []
    for brand in brands:
        for material in brand["materials"]:
            if material in unique_trending_materials:
                trending_materials_lst.append(material)
            else:
                unique_trending_materials.add(material)
    return trending_materials_lst

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print("---Problem 3---")
print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))

def find_best_fabric_pair(fabrics, budget):
    # Time Complexity: O(n log n), because sorting the fabrics takes O(n log n) and the two-pointer approach takes O(n)
    # Space Complexity: O(n * m), because there can be m materials for n fabrics
    sorted_fabrics = sorted(fabrics, key=lambda x: x[1])
    left, right = 0, len(sorted_fabrics) - 1
    best_pair = (None, None)
    max_cost = 0
    
    while left < right:
        current_sum = sorted_fabrics[left][1] + sorted_fabrics[right][1]
        if current_sum > budget:
            right -= 1
        elif current_sum <= budget:
            if current_sum > max_cost:
                max_cost = current_sum
                best_pair = (sorted_fabrics[left][0], sorted_fabrics[right][0])
            left += 1
    return best_pair
    
fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print("---Problem 4---")
print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))