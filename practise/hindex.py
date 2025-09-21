n = int(input())
citations = [int(input()) for _ in range(n)]

# Sort citations in descending order
citations.sort(reverse=True)

h_index = 0
for i, c in enumerate(citations, start=1):
    if c >= i:
        h_index = i
    else:
        break

print(h_index)
