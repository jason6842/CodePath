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