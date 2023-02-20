num = input("Enter your number: ")

nums = num.split("0")

evens = list(filter(lambda x: int(x) % 2 == 0, nums))

total = sum(map(int, evens))
avg = total / len(evens)

print(f"{'+'.join(evens)}={total}")
print(f"{total}/{len(evens)}={avg}")