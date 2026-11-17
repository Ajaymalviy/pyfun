S = "ababAbB"
upper = 0
lower = 0

for i in S:
    if i.isupper():
        upper +=1
    else:
        lower +=1

print("upper letters are : ", upper, "Lower are : ", lower)
