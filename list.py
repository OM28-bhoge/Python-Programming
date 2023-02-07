################

# 1. who is winner?
Doremon = [75, 10, 34, 70, 90]
Shinchan = [56, 89, 12, 90, 45]
def find_winner(Doremon , Shinchan):
    Doremon_wins = 0
    Shinchan_wins = 0
    for i in range(len(Doremon)):
        if Doremon[i] > Shinchan[i]:
            Doremon_wins += 1
        elif Shinchan[i] > Doremon[i]:
            Shinchan_wins += 1
    if Doremon_wins > Shinchan_wins:
        return "Doremon", Doremon_wins
    elif Shinchan_wins > Doremon_wins:
        return "Shinchan", Shinchan_wins
    else:
        return "tie", Doremon_wins
result = find_winner(Doremon, Shinchan)
print("The winner is", result[0], "with", result[1],"wins")
#output = "Doremon", 3

###############

###############

# 2. where are you at current position?

up_down = ["D", "U", "D", "D", "U", "D", "D", "D", "U"]
position = 0
for move in up_down:
    if move == "U":
        position += 1
    else:
        position -= 1

print("Current position:", position)
#output = -3

###############

# 3. find difference
lists = [[15,27,13],
        [49,25,62],
        [70,81,92]]

differences = [[lists[i][j]-lists[i-1][j] for j in range(len(lists[i]))] for i in range(1,len(lists))]
print(differences)

###############

# 4. find ratio of positive, negative, zeros
numbers = [15,-25,0,45,34,0,-6,-23]

def count_ratios(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
            
    total = len(numbers)
    
    positive_ratio = positive_count / total
    negative_ratio = negative_count / total
    zero_ratio = zero_count / total
    return positive_ratio, negative_ratio, zero_ratio

print(count_ratios(numbers))	
        
###############

# 5. find minimum and maximum sum
numbers = [45, 30, 23, 10, 67, 45]
min_sum = min(sum(numbers[:i]+numbers[i+1:]) for i in range(len(numbers)))
max_sum = max(sum(numbers[:i]+numbers[i+1:]) for i in range(len(numbers)))
print(f"Minimum sum: {min_sum}")
print(f"Maximum sum: {max_sum}")

#sum_minimum = 0

#sum_maximum = 0

###############

# 6. write a code in python crash highest tower(s)
#[5,9,6,2,7,9]
def crash_highest_towers(towers):
    max_height = max(towers)
    return [i for i, j in enumerate(towers) if j == max_height]

towers = [5,9,6,2,7,9]
highest_towers = crash_highest_towers(towers)

print("Towers to be crashed:",highest_towers)

###############

# 7. increase marks
def increase_marks(marks):
    increased_marks = [mark + 10 for mark in marks]
    return increased_marks

marks = [79,20,45,56,92]
new_marks = increase_marks(marks)

print("Increased Marks:", new_marks)