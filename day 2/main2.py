import re

lists = []
sum = 0

with open("D:\Dipu\Practice\Python\Advant of code\day 2\input.txt", "r") as f:
    for i in f.readlines():
        red_max = 0
        blue_max = 0
        green_max = 0

        li = re.split(r'[:;,]', i.strip())
        for j in li:

            list = j.strip().split(" ")
            
            if "red" in list[1]:
                red_max = max(red_max, int(list[0]))

            if "blue" in list[1]:
                blue_max = max(blue_max, int(list[0]))

            if "green" in list[1]:
                green_max = max(green_max, int(list[0]))

        sum = sum + (red_max * blue_max * green_max)

print(sum)