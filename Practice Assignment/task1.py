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
        
        
