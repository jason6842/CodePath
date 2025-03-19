# Problem 1
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    def add_item(self, item_name):
        valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_items:
            self.furniture.append(item_name)

def of_personality_type(townies, personality_type):
    villager_type_list = []
    for villager in townies:
        if villager.personality == personality_type:
            villager_type_list.append(villager.name)

    return villager_type_list

def message_received(start_villager, target_villager):
    curr = start_villager.neighbor
    while curr != None:
        if curr == target_villager:
            return True
        curr = curr.neighbor
    return False


# print("-----Problem 1-----")
# apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)

# print("-----Problem 2-----")
# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# print("-----Problem 3-----")
# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# print("-----Problem 4-----")

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# Add code here to link the above nodes
print("-----Problem 5-----")
isabelle = Node("Isabelle")
saharah = Node("Saharah", isabelle)
harriet = Node("Harriet", saharah)
kk_slider = Node("K.K. Slider", harriet)
print_linked_list(kk_slider)



def catch_fish(head):
    if head:
        print(f"I caught a {head.value}!")
        return head.next
    print("Aw! Better luck next time!")


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print("-----Problem 6-----")
print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))

def fish_chances(head, fish_name):
    list_len = 0 
    fish_count = 0 
    
    curr = head 
    while curr: 
        list_len += 1 
        if curr.value == fish_name:
            fish_count += 1
        curr = curr.next
    # round(number, 2)
    return round(fish_count / list_len, 2)

print("-----Problem 7-----")
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))

def restock(head, new_fish):
    curr = head   
    while curr.next:
        curr = curr.next
    
    curr.next = Node(new_fish)
    return head

print("-----Problem 8-----")
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))