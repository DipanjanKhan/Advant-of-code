with open("D:\Dipu\Practice\Python\Advant of code\day 1\input.txt", "r") as f:
    str = list(f.readlines())

sum = 0

for i in str:
    num = [char for char in i if char.isdigit()]
    sum = sum + int(num[0]+num[-1])

print(sum)