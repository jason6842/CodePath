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

print("----------Problem 1----------")
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

print("----------Problem 2----------")
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

print("----------Problem 3----------")
print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))

# Problem 4
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

print("----------Problem 4----------")
print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

# Problem 5
def organize_fabrics(fabrics):
    # Time Complexity: O(n * n) where n is the number of fabrics * the number of fabrics on the stack that needs to be sorted
    # Space Complexity: O(n)
    stack = []
    for fabric in fabrics:
        if stack and stack[-1][1] < fabric[1]:
            temp_storage = []
            while stack and stack[-1][1] < fabric[1]:
                temp_storage.append(stack.pop())
            stack.append(fabric)
            # print("TEMP STORAGE: ", temp_storage)
            for temp in temp_storage[::-1]:
                stack.append(temp)
        else:
            stack.append(fabric)
    return [fabric for fabric, eco in stack]

# Same runtime complexity except slightly cleaner code
def organize_fabrics(fabrics):
    stack = []
    for fabric in fabrics:
        # do not need if statement since while loop already does so
        temp_stack = []
        while stack and stack[-1][1] < fabric[1]:
            temp_stack.append(stack.pop())

        # no else statement since both while loops has its own condition
        stack.append(fabric)
        
        # instead of reverse iteration, just use stack again
        while temp_stack:
            stack.append(temp_stack.pop())

    # doesn't really matter, fabric[0] or unpacking method
    return [fabric[0] for fabric in stack]

fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print("----------Problem 5----------")
print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))

# Problem 6
from collections import deque
# def process_supplies(supplies):
#     # Time Complexity:
#     # Space Complexity:
#     queue = deque()
#     for supply in supplies:
#         temp_queue = deque()
#         while queue and queue[0][1] < supply[1]:
#             temp_queue.append(queue.popleft())

#         queue.append(supply)
#         # print(temp_queue)
#         while temp_queue:
#             queue.append(temp_queue.popleft())

#     return [supply[0] for supply in queue]

def process_supplies(supplies):
    # Time Complexity: O(n * n)
    # Space Complexity: O(n)
    queue = deque()
    for supply in supplies:
        # a flag for if the value is in its correct place
        inserted = False
        temp_queue = deque()

        # iterates through the current queue
        while queue:
            # If the current supply has a higher priority than the first item in the queue,
            # insert it before lower-priority elements.
            if not inserted and queue[0][1] < supply[1]:
                # Add the new supply to the temporary queue before the lower-priority element
                temp_queue.append(supply)
                inserted = True # Mark that the supply has been placed

            # Move the next element from the original queue to the temp queue
            # This ensures that all previously existing elements remain in order
            # Larger elements would still be in the front, but ensures that the largest supply
            # will be in the front (with new supply included)
            temp_queue.append(queue.popleft())
        
        # if the current supply was never inserted, than it is the smallest value
        if not inserted:
            temp_queue.append(supply)
        # queue should be in its current sorted order with the new supply
        queue = temp_queue

    return [supply[0] for supply in queue]


supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

print("----------Problem 6----------")
print(process_supplies(supplies))
print(process_supplies(supplies_2))
print(process_supplies(supplies_3))