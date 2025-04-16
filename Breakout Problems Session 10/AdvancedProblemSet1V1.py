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

# Problem 1
def find_max(head):
    """
        U: Find the max value of the linked list
        M: Traversing
        P: Traversing the linked list and have a variable for the current max
    """
    if head is None:
        return None
    max_value = float('-inf')
    curr = head

    while curr:
        max_value = max(max_value, curr.value)
        curr = curr.next

    return max_value

head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))

# Problem 2
def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head


head = Node("Isabelle", Node("Alfonso", Node("Cyd")))


# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

# Problem 3
def delete_dupes(head):
    # Time Complexity:
    # Space Complexity:
    """
        U: Sorted linked list
        M:
        P: Set for unique nodes, prev pointer starts at None, and curr pointer 
        # Linked List: 3 -> 3 -> 3 -> 3 ->4 -> 5
                    p
                                    c
                    set : 1,2,3
                    if c != c.next
                        prev
                    else: 
                        c = c.next

                    1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 5
                         p
                                        c    
    """                                     

    # TRY USING A WHILE LOOP TO SKIN THE DUPLICATES
            

    


head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

head1 = Node(1, Node(2, Node(3, Node(3, Node(3, Node(4, Node(5)))))))

print_linked_list(head1)

print_linked_list(delete_dupes(head1))


# Problem 4
def has_cycle(head):
    # Time Complexity: O(n), where fast loops the entire linked list to catch up to slow
    # Space Complexity: O(1)
    if head is None:
        return None
    slow = head
    fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # can be None on last iteration so best to check if it points to the same memory instead of value
        if fast == slow: 
            return True
    return False

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

print(has_cycle(peach))

# Problem 5
def remove_nth_from_end(head, n):
    if head is None:
        return None
    
    slow = head
    fast = head

    while fast and n > 0:
        fast = fast.next
        n -= 1

    if fast is None:
        return head.next

    while fast:
        # slow = slow.next
        fast = fast.next
        if fast == None:
            break
        else:
            slow = slow.next

    slow.next = slow.next.next # skip one node

    return head

head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
"""
Rainbow Trout -> Ray
        s
                  f
"""
print_linked_list(remove_nth_from_end(head3, 1))