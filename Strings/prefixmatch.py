fixed = input("Enter fixed string: ")
rotatable = input("Enter rotatable string: ")
n = len(rotatable)
answer = float('inf')
for i in range(n):
    rotated = rotatable[i:] + rotatable[:i]
    if rotated.startswith(fixed):
        left_rotation = i
        right_rotation = n - i
        answer = min(answer, left_rotation, right_rotation)
if answer == float('inf'):
    print("Not possible")
else:
    print("Minimum rotations required:", answer)