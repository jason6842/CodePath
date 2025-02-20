# Problem 1
def welcome():
    print("Welcome to the Hundred Acre Wood!")

welcome()

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greeting("Michael")
greeting("Winnie the Pooh")

"""
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

Character	Catchphrase
"Pooh"	"Oh bother!"
"Tigger"	"TTFN: Ta-ta for now!"
"Eeyore"	"Thanks for noticing me."
"Christopher Robin"	"Silly old bear."
If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"
"""
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


print_catchphrase("Pooh")
print_catchphrase("Piglet")

def get_item(items, x):
    if len(items) > x:
        
        return print(items[x])
    else:
        
        return print("None")
    
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

# Problem 5
def sum_honey(hunny_jars):
    total = 0
    for honey in hunny_jars:
        total += honey
    return total

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))


# Problem 6
def doubled(hunny_jars):
    return [x * 2 for x in hunny_jars]

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

# Problem 7
def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

# Problem 8
def print_todo_list(task):
    print("Pooh's To Dos")
    for i in range(len(task)):
        print(f"{i + 1}. {task[i]}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

# Problem 9
def can_pair(item_quantities):
    for item in item_quantities:
        if item % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

# Problem 10
def split_haycorns(quantity):
    res = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            res.append(i)
    return res

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity)) 

# Problem 11
def tiggerfy(s):
    return "".join(c for c in s if c.lower() not in "tigger")

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

#Problem 12
def locate_thistles(items):
    return [i for i in range(len(items)) if items[i] == "thistle"]

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))