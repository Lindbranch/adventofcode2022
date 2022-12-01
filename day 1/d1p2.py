f = open("calories.txt", "r")
newTotal = 0
allCalories = []

for x in f:
    if x.isspace():
        allCalories.append(newTotal)
        newTotal = 0
    else:
        x = int(x)
        newTotal = x + newTotal
print(sum(sorted(allCalories)[-3:]))