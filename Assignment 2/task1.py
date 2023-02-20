name = input("What is your name? ")

name_upper = name.upper()

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for char in name_upper:
    if char == 'A':
        a_count += 1
    elif char == 'E':
        e_count += 1
    elif char == 'I':
        i_count += 1
    elif char == 'O':
        o_count += 1
    elif char == 'U':
        u_count += 1


print(f"There are {len(name)} characters in your name.")
print(f"The number of times 'A' occurs in your name is {a_count}")
print(f"The number of times 'E' occurs in your name is {e_count}")
print(f"The number of times 'I' occurs in your name is {i_count}")
print(f"The number of times 'O' occurs in your name is {o_count}")
print(f"The number of times 'U' occurs in your name is {u_count}")