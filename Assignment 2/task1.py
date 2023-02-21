name= list(input("what is your name?"))
print(name)
cnt=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0
for i in range(0,len(name)):
    if name[i]== 'a' or name[i]== 'A':
        cnt+=1

    elif name[i]== 'e' or name[i]== 'E':
        cnt2+=1

    elif name[i]== 'i' or name[i]== 'I':
        cnt3+=1
        
    elif name[i]== 'o' or name[i]== 'O':
        cnt4+=1
        
    elif name[i]== 'u' or name[i]== 'U':
        cnt5+=1



    
    
print("The number of times 'A' occurs in your name is:",cnt)
print("The number of times 'E' occurs in your name is:",cnt2)
print("The number of times 'I' occurs in your name is:",cnt3)
print("The number of times 'O' occurs in your name is:",cnt4)
print("The number of times 'U' occurs in your name is:",cnt5)