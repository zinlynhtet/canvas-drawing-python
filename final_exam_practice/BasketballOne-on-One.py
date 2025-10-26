record = input().strip()

scoreA = 0
scoreB = 0

for i in range(0, len(record), 2):
    player = record[i]
    points = int(record[i + 1])
    
    if player == 'A':
        scoreA += points
    else:
        scoreB += points

if scoreA > scoreB:
    print("A")
else:
    print("B")
