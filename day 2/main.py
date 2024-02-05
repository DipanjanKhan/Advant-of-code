import re

with open("D:\Dipu\Practice\Python\Advant of code\day 2\input.txt",'r') as f:
    str = f.readlines()

no = 0
count = 0
for i in str:
    no += 1
    blue = 0
    green = 0
    red = 0
    for j in range(len(i)):
        if i[j] == "b":
            st = i[j-4: j]
            blue = int(re.findall(r"\d",st)[0]) + blue
        if i[j] == "r":
            st = i[j-4: j]
            red = int(re.findall(r"\d",st)[0]) + red
        if i[j] == "g":
            st = i[j-4: j]
            green = int(re.findall(r"\d",st)[0]) + green
    if red <= 12 and green <= 13 and blue <= 14:
        count += no
        print(no)
    
print(count)