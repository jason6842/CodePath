# Session #1 Advanced Problem Set Version 2
def predictAdoption_victory(votes):
    # "CDD"
    # 1. "C" -> [C]
    # 2. "D" -> [ ]
    # 3. "D" -> [D]

    # "CD"
    # 1. "C" -> [C]
    # 2. "D" -> [ ]
    queue = []
    # prev value or last value in the queue at end of loop
    prev_val = 0
    for vote in votes:
        if not queue or queue[0] == vote:
            queue.append(vote)
        else:
            prev_val = queue.pop(0)
        
    if len(queue) == 0:
        if prev_val == "C":
            return "Cat Lovers"
        else:
            return "Dog Lovers"
    else:
        if queue[0] == "C":
            return "Cat Lovers"
        else:
            return "Dog Lovers"

    
print(predictAdoption_victory("CD")) 
print(predictAdoption_victory("CDD")) 
print(predictAdoption_victory("CDDC"))

print("(dribtacgod)"[::-1])
print("(!(love(stac))I)"[::-1])
print("adopt(yadot(a(tep)))!"[::-1])


# Problem 3
def rearrange_animal_names(s):
    stack = []

    for c in s:
        if c != ')':
            stack.append(c)
        elif c == ')':
            word = ''
            while stack and stack[-1] != '(':
                word += stack[-1]
                stack.pop()
            stack.pop() # removes '('
            stack.append(word[::-1]) 
        print(stack)
    return ''.join(stack)[::-1]
    
print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 

