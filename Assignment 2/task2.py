count=0
String = input("Enter the String:")
Word=input("Enter the Word:")
for letter in String.split():
    if Word == letter:
        count+=1
print(count,"times")
