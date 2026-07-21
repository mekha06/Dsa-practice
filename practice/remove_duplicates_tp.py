nums = list(map(int, input("Enter the elements: ").split()))
l = 0
for r in range(1, len(nums)):
    if nums[l] != nums[r]:
        l += 1
        nums[l] = nums[r]
print("Unique elements:", nums[:l+1])
print("Count:", l + 1)
