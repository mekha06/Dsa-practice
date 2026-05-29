#Find maximum subarray sum.
arr=list(map(int,input("enter the array elements : ").split()))
curr_sum=arr[0]
max_sum=arr[0]
for i in range(1,len(arr)):
    curr_sum=max(arr[i],curr_sum+arr[i])
    max_sum=max(max_sum,curr_sum)
print("th maximum sum of subarray : " ,max_sum)

"""
-----------------------------------Output-----------------------------------------------
enter the array elements : -2 1 -3 4 -1 2 1 -5 4
th maximum sum of subarray :  6

-----------------------------------------------------------------------------------------
Dry run table:
| Index | Element | `current_sum + arr[i]` | `current_sum` | `max_sum` |
| ----- | ------- | ---------------------- | ------------- | --------- |
| 0     | -2      | —                      | -2            | -2        |
| 1     | 1       | -1                     | 1             | 1         |
| 2     | -3      | -2                     | -2            | 1         |
| 3     | 4       | 2                      | 4             | 4         |
| 4     | -1      | 3                      | 3             | 4         |
| 5     | 2       | 5                      | 5             | 5         |
| 6     | 1       | 6                      | 6             | 6         |
| 7     | -5      | 1                      | 1             | 6         |
| 8     | 4       | 5                      | 5             | 6         |

"""