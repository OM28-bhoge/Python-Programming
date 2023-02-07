numbers = [10, 20, 30, 20, 40, 60, 20, 60, 80]
count_dict = {}
for number in numbers:
    if number in count_dict:
        count_dict[number] += 1
    else :
        count_dict[number] = 1
print(count_dict) 