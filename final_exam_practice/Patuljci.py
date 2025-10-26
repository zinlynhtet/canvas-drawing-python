nums = [int(input()) for _ in range(9)]
total_sum = sum(nums)
to_remove = total_sum - 100

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if nums[i] + nums[j] == to_remove:
            fake1, fake2 = nums[i], nums[j]
            found = True
            break
    if found:
        break

for num in nums:
    if num not in [fake1, fake2]:
        print(num)
