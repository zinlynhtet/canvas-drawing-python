s = input().strip()

stack = []

balanced = True

for char in s:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if not stack:
            balanced = False
            break
        stack.pop()

# If stack is empty and no mismatches, it's balanced
if stack:
    balanced = False

print(balanced)
