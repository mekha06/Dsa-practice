a=list(map(int, input("enter the array elements:").split()))
def move_zeros(arr):
  l=0
  for r in range(len(arr)):
    if arr[r]!=0:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
  return arr
print(move_zeros(a))
        