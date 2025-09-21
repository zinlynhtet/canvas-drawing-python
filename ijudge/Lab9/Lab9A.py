s = input("Enter a string: ").strip()

freq = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
for ch in s:
    freq[ch] += 1

for c in "abcdefghijklmnopqrstuvwxyz":
    if freq[c] > 0:
        print(c, freq[c])
