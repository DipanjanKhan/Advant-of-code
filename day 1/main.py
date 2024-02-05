with open("input.txt", "r") as f:
    str = list(f.readlines())

num = []
num2 = []
sum = 0
value = 0
for i in str:
    num = [char for char in i if char.isdigit()]
    num2.append(num)

for i in num2:
    value = int(i[0]+i[-1])
    sum = sum + value
print(sum)



