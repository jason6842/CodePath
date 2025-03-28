# Problem 3
"""
A well-intentioned reader has improperly put back a book on the shelf.
 Given the head of a linked list shelf where each node represents a book on the shelf, 
 and a value k return the head of the linked list after swapping the values of the kth node from the 
 beginning and the kth node from the end. Assume the list is 1-indexed. Assume 1 <= k < n where n is the length of shelf.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def swap_books(shelf, k):
    """
        slow_prev = Node(0)
        slow_prev.next = shelf
        slow = shelf
        fast_prev = Node(0)
        fast_prev.next = shelf
        fast = shelf

        while k - 1 > 1:
            fast_prev = fast
            fast = fast.next
    """
    slow = Node(0)
    slow.next = shelf
    fast = shelf

    length = k
    while length - 1 > 1:
        fast = fast.next
        length -= 1

    k_begin_prev = fast # 1
    fast = fast.next # 2

    k_end_prev = None # 3
    while fast:
        k_end_prev = slow
        slow = slow.next
        fast = fast.next
    
    k_begin = k_begin_prev.next
    k_end_next = slow.next

    temp = k_begin_prev.next.next # 3
    k_begin_prev.next = slow # 4
    slow.next = temp # 4 -> 3

    k_end_prev.next = k_begin # 2
    k_begin.next = k_end_next


    print(k_begin_prev.value) # 1
    print(k_end_prev.value) # 3
    print(slow.value) # 4
    # 1 -> 2 -> 3 -> 4 -> 5
    return shelf


shelf = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5', Node('Book 6'))))))

print_linked_list(swap_books(shelf, 2))

shelf1 = Node('Book 1', Node('Book 2'))

print_linked_list(swap_books(shelf1, 1))