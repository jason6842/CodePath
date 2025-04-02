# Problem 1
def count_layer(sandwich):
    # Time Complexity: O(n)
    # Space Complexity: O(n), where n is n recursive calls on the call stack
    if len(sandwich) == 1:
        return 1

    return 1 + count_layer(sandwich[1])

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layer(sandwich1))
# print(count_layer(sandwich2))

# Problem 2
def reverse_orders(orders):
    # Time Complexity: O(n)
    # Space Complexity: O(n + k)
    reverse_orders = []
    order_list = orders.split(" ")
    
    def reverse_str(orders):
        nonlocal reverse_orders

        if len(orders) == 0:
            return

        reverse_orders.append(orders[-1])
        return reverse_str(orders[:-1])
    
    reverse_str(order_list)
    return ' '.join(reverse_orders)

# def reverse_orders(orders):
    # Time Complexity: O(n)
    # Space Complexity: O(n + k)
#     reverse_orders = []
#     order_list = orders.split(" ")
    
#     def reverse_str(reverse_orders, orders):
#         if len(orders) == 0:
#             return

#         reverse_orders.append(orders[-1])
#         return reverse_str(reverse_orders, orders[:-1])
    
#     reverse_str(reverse_orders, order_list)
#     return ' '.join(reverse_orders)

print(reverse_orders("Bagel Sandwich Coffee"))

def can_split_coffee(coffee, n):
    # Time Complexity: O(n)
    # Space Complexity: O(n), because of call stack
    if len(coffee) == 0:
        return True
    
    if coffee[0] % n == 0:
        return can_split_coffee(coffee[1:], n)
    else:
        return False
    


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))

# Problem 4
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

def merge_orders(sandwich_a, sandwich_b):
    # CONFUSED
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    
    a_next = sandwich_a.next
    b_next = sandwich_b.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(a_next, b_next)
    return sandwich_a

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
# print_linked_list(merge_orders(sandwich_a, sandwich_c))
