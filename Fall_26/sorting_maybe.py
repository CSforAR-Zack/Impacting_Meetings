nums: list[int] = [5, 2, 8, 1, 9, 3]
length: int = len(nums)

for i in range(length):
    for j in range(length):
        if nums[i] < nums[j]:
            temp: int = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

print(nums)
