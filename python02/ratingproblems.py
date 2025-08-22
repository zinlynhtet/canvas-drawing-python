n, k = map(int, input().split())
ratings = [float(input()) for _ in range(k)]

total_rating = sum(ratings)
remaining_judge = n - k

min_avg = (total_rating + remaining_judge * (-3)) / n

max_avg = (total_rating + remaining_judge * (+3)) / n

print(f"{min_avg:.4f} {max_avg:.4f}")
 