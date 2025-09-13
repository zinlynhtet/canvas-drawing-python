s = input().strip()

stack = []
top = -1 
balanced = True

for char in s:
    if char == '(':
        top = top + 1
        try:
            stack[top] = '('
        except IndexError:
            stack.append('(')
    elif char == ')':
        if top == -1:
            balanced = False
            break
        top = top - 1

if top != -1:
    balanced = False

print(balanced)
