# Problem 1
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front is None:
            return True
        return False


    def enqueue(self, next_song):
        new_node = Node(next_song)
        if self.rear: # if there is a tail, we just add to the end of tail
            self.rear.next = new_node
            self.rear = self.rear.next
        else:
            self.front = new_node
            # self.front.next = self.rear
            self.rear = new_node

        # 1 -> 1
    
    def dequeue(self):
        if self.is_empty():
             return None
        
        if self.front:
            deleted_value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return deleted_value


        
    
    def peek(self):
        if self.is_empty():
             return None
        return self.front.value
    

# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 


# ('Hug from a Dinosaur', 'Torres')
# Peek:  ('Hug from a Dinosaur', 'Torres')
# Dequeue:  ('Hug from a Dinosaur', 'Torres')
# Dequeue:  None
# Is Empty:  False
# Dequeue:  None
# Is Empty: False