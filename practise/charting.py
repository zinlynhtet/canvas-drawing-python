def process_log(log):
    rows = len(log)
    cols = len(log[0])
    # Extract columns
    columns = ["".join(log[r][c] for r in range(rows)) for c in range(cols)]
    # Sort columns by the last '*' row (bottom to top), empty columns at the end
    def col_key(col):
        for i in reversed(range(rows)):
            if col[i] == '*':
                return rows - i  # Changed to reverse order (bottom to top)
        return float('inf')  # No '*' goes to the end, not front
    columns.sort(key=col_key)
    # Rebuild rows
    return ["".join(col[r] for col in columns) for r in range(rows)]

logs = []
current = []

while True:
    try:
        line = input()
    except EOFError:
        break

    if line.strip() == "":
        if current:
            logs.append(current)
            current = []
    else:
        current.append(line)

if current:
    logs.append(current)

for i, log in enumerate(logs):
    result = process_log(log)
    for row in result:
        print(row)
    if i < len(logs) - 1:
        print()
