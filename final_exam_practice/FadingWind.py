def simulate_paper_airplane(h, k, v, s):
    """
    Simulates the paper airplane flight and returns horizontal distance traveled.
    
    Args:
        h: starting height
        k: critical velocity factor
        v: starting velocity
        s: wind strength
    
    Returns:
        Total horizontal distance traveled
    """
    distance = 0

    while h > 0:
        # Step 1: Increase v by s
        v += s

        # Step 2: Decrease v by max(1, floor(v/10))
        decrease_amount = max(1, v // 10)
        v -= decrease_amount

        # Step 3: Check velocity conditions and update h
        if v >= k:
            # If v >= k, increase h by one
            h += 1
        elif 0 < v < k:
            # If 0 < v < k, decrease h by one
            h -= 1
            # If h is zero after decrease, set v to zero
            if h == 0:
                v = 0
        else:
            # If v <= 0, set h to zero and v to zero
            h = 0
            v = 0

        # Step 4: Travel horizontally by v units (only if still flying)
        if h > 0:
            distance += v

        # Step 5: Decrease s by 1 if s > 0
        if s > 0:
            s -= 1

    return distance


# Read input
input_line = input().strip()
h, k, v, s = map(int, input_line.split())

# Simulate and output result
result = simulate_paper_airplane(h, k, v, s)
print(result)
