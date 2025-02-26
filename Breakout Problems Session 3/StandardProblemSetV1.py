"""
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass
Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

Initialize a stack to keep track of the opening tags as you encounter them.
Iterate through the posts
If it's an opening tag, push it onto the stack
If it's a closing tag, check if the stack is not empty and whether the tag at the top of the stack is the corresponding opening tag
If yes, pop the opening tag from the stack (we've found its match!)
If no, the tags are not properly nested and we should return False
After processing all characters, if the stack is empty, all tags were properly nested and we should return True. If the stack is not empty, some opening tags were not closed, so return False
"""
def is_valid_post_format(posts):
    stack = []

    for c in posts:
        if c in "{([":
            stack.append(c)
        elif c in "}])":
            if len(stack) != 0:
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

    return len(stack) == 0

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))


"""
You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, you want to remove any pairs of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.

def clean_post(post):
  pass
Example Usage:

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
Example Output:

post

s

How do we know which data structure and/or algorithm to use when solving this problem? Should we use a stack? A queue? Two pointer? None of the above?

For this problem, a stack would be a good choice because we're checking for the 'balance' of pairs of symbols:

Checking and Removing Pairs
As we traverse the string, we can look at each letter one by one.
If the letter we're looking at can pair up with the last letter you added to the stack (like "aA"), we can remove that last letter from the stack. This is like taking the top plate off the pile.
If it doesn't form a pair, we can add the new letter on top of the stack, like putting another plate on top.
Rechecking After Removal
After we remove a pair, the stack might have a new top letter that could potentially form another pair with the next letter we examine. A stack allows us to handle this smoothly because we only ever look at the top of the stack and the next letter.
For more information about common use cases of stacks, queues, and two pointer, take a look at the unit cheatsheet.
"""

def clean_post(post):
    stack = []
    for c in post:
        if stack and c.lower() == stack[-1].lower():
            if c.isupper()  and stack[-1].islower():
                stack.pop()
            elif c.islower() and stack[-1].isupper():
                stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 


# Problem 6
def edit_post(post):
    words = post.split()
    res = []

    for word in words:
        queue = list(word)
        reverse_word = ""
        for i in range(len(queue)):
            reverse_word += queue.pop()
        res.append(reverse_word)

    return " ".join(res)


print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 