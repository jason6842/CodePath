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
def edit_dna_sequence(dna_strand, m, n):
    # Case for removing the head
    dummy = Node(0)
    dummy.next = dna_strand
    
    prev = dummy
    curr = dna_strand

    keep_counter = m
    delete_counter = n

    while curr:
        # Keep
        while keep_counter > 0:
            # walking the nodes iterate through list
            if curr is None:
                return dummy.next
            prev = prev.next
            curr = curr.next
            keep_counter -= 1

                 
        # Remove
        while curr and delete_counter > 0:
            # only move curr forward
            curr = curr.next
            delete_counter -= 1

        keep_counter = m
        delete_counter = n

        prev.next = curr


    return dummy.next
    

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

# Problem 2
def cycle_length(protein):
    """
    Ala -> Gly -> Leu -> Val -> Bro
            ^             |
    """
    slow, fast = protein, protein

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    if not fast:
        return []

    slow = slow.next
    
    cycle_lst = []

    while slow != fast:
        cycle_lst.append(slow.value)
        slow = slow.next
    cycle_lst.append(fast.value)
    
    return cycle_lst

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))

# Problem 3
def split_protein_chain(protein, k):
    protein_length = 0
    curr = protein
    while curr:
        curr = curr.next
        protein_length += 1

    segment_length = protein_length // k\
    
    # [a, b, c, d, e], [a, b, c, d, e], [a, b]