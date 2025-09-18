mapping = {
    'a': "2",    'b': "22",   'c': "222",
    'd': "3",    'e': "33",   'f': "333",
    'g': "4",    'h': "44",   'i': "444",
    'j': "5",    'k': "55",   'l': "555",
    'm': "6",    'n': "66",   'o': "666",
    'p': "7",    'q': "77",   'r': "777", 's': "7777",
    't': "8",    'u': "88",   'v': "888",
    'w': "9",    'x': "99",   'y': "999", 'z': "9999",
    ' ': "0"
}

n = int(input().strip())
for case in range(1, n + 1):
    text = input().rstrip("\n")   # keep spaces inside message
    result = ""
    prev_digit = ""

    for ch in text:
        code = mapping[ch]
        # Pause if same digit as before
        if prev_digit == code[0]:
            result += " "
        result += code
        prev_digit = code[0]

    print(f"Case #{case}: {result}")
