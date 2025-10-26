m1, m2, f = map(int, input().split())

final_score = 0.25 * m1 + 0.25 * m2 + 0.5 * f

if final_score >= 90:
    print("A")
elif final_score >= 80:
    print("B")
elif final_score >= 70:
    print("C")
elif final_score >= 60:
    print("D")
else:
    print("F")
