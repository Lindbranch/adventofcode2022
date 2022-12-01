f = open("calories.txt", "r")
highestTotal = 0
newTotal = 0
for x in f:
    if x.isspace():
        if newTotal > highestTotal:
            highestTotal = newTotal
            newTotal = 0
        else:
            newTotal = 0
    else:
        x = int(x)
        newTotal = x + newTotal
print(highestTotal)