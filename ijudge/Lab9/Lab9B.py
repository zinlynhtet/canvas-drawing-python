s = input().strip()

words = s.split()

unique_sorted = sorted(set(words))

for w in unique_sorted:
    print(w)
