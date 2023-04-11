list1=[2,3,4,4,4,5,6]
list2=[3,4,4,5,7]
c = []
i, j = 0, 0
while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
        c.append(list1[i])
        i += 1
        j += 1
    elif list1[i] > list2[j]:
        j += 1
    else:
        i+=1

print(c)