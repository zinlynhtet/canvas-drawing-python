parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        parent[root_y] = root_x

while True:
    line = input().strip()
    if line == "$":
        break
    a, b = line.split()
    for w in (a, b):
        if w not in parent:
            parent[w] = w
    union(a, b)

groups = {}
for w in parent:
    root = find(w)
    if root not in groups:
        groups[root] = []
    groups[root].append(w)

result = [sorted(words) for words in groups.values()]
result.sort()

for group in result:
    print(" ".join(group))
