n = int(input().strip())
alphabet = set("abcdefghijklmnopqrstuvwxyz")

for _ in range(n):
    phrase = input().lower()
    present = {ch for ch in phrase if 'a' <= ch <= 'z'}
    if missing := sorted(alphabet - present):
        print("missing", "".join(missing))
    else:
        print("pangram")
