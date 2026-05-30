height=list(map(int,input("enter the elements of the array : ").split()))
n=len(height)
left=0
right=n-1
max_water=0
while left < right:
    width=right-left
    current_water=min(height[left] , height[right]) * width
    max_water= max(current_water , max_water)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print("maximum water stored :", max_water)


"""
---------------------------------------------Output-------------------------------------------

enter the elements of the array : 1 8 6 2 5 4 8 3 7
maximum water stored : 49

TC=O(n)

---------------------------------------------------------------------------------------------

Its a two pointer pattern question!
Index :  0 1 2 3 4 5 6 7 8
Height: [1 8 6 2 5 4 8 3 7]

 8 |     |               |
 7 |     |               |       |
 6 |     |   |           |       |
 5 |     |   |     |     |       |
 4 |     |   |     | |   |       |
 3 |     |   |     | |   | |     |
 2 |     |   | |   | |   | |     |
 1 | |   |   | |   | |   | |     |
   +-------------------------------
     1   8   6 2   5 4   8  3    7 
              indexing
     0   1   2 3   4 5   6  7    8 
x axis is at 1 unit distance ; in the image it may appear irregular but its 1 unit actually.
here left=0 and right=8 (n-1)

1. just see we can calculate the width from right - left and the height would be the minimum height
   of left and right; eg : l=1 and r =7(indices of 1 and 7 are 0 and 8 ;8-0 as per formula given below )
   would be chosen for the formula: which gives the area    
      current_water = min(height[left], height[right]) * width

2. we will be intializing max_water = 0 at first; it will be updated as:
      max_water = max(max_water, current_water)

3.finally the max_water would be printed
 
Its is two pointer approach where we use left and right pointers to traverse and update 
them according to condition in the code. 

"""