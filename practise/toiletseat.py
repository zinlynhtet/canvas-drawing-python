s = input().strip()

# Policy 1: always leave seat UP
count1 = 0
seat = s[0]
for i in range(1, len(s)):
    if seat != s[i]:
        count1 += 1
    if s[i] != 'U':
        count1 += 1
    seat = 'U'
# Policy 2: always leave seat DOWN
count2 = 0
seat = s[0]
for i in range(1, len(s)):
    if seat != s[i]:
        count2 += 1
    if s[i] != 'D':
        count2 += 1
    seat = 'D'
# Policy 3: leave seat as you found it
count3 = 0
seat = s[0]
for i in range(1, len(s)):
    if seat != s[i]:
        count3 += 1
    seat = s[i]

print(count1)
print(count2)
print(count3)
