# Problem 1
def arrange_guest_arrival_order(arrival_pattern):
    """
    U: if 'I', next guest should have a higher status than the previous one,
       if 'D', next guest should have a lower status than the previous one

    M: Stack
    P:
        Theory #1: What if I add the digits from 1 to 9 onto the stack, if it is an 'I', get from the bottom of the stack,
        and if it is 'D', pop from the top of the stack
    I: 1. Add each value onto the stack
       2. If the letter is 'I', pop each value from the stack and add it to guess_order.
       3. If the letter is 'D', nothing happens besides adding the value to to the stack
       4. If i reached the end, pop the rest of the values from the stack and add it to guest_order.
    R:
    E:
    """
    digits = [str(x + 1) for x in range(len(arrival_pattern) + 1)]
    stack = []
    guest_order = ""

    for i in range(len(arrival_pattern) + 1): # n + 1
        stack.append(digits[i])

        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                guest_order += stack.pop()
        print(stack, i, guest_order)
    return guest_order
    

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  