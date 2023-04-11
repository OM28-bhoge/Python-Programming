list = [1 , 8 , 6 , 2 , 5 , 4 , 8 , 3 , 7] #output = 49

left = 0;
right = 1;
max_area = 0;

while left < right:
    width = right - left
    height = min(list[left], list[right])
    area = width * height 
    max_area = max(max_area, area)
    if list[left] < list[right]:
            left += 1
    else:
        right -= 1

print(max_area)