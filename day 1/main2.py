import re

lists = []
lists2 = []
dicts = { "one":"1ne", "two":"2wo", "three":"3hree", "four":"4our", "five":"5ive", "six":"6ix", "seven":"7even", "eight":"8ight", "nine":"9ine" }
num_string =  "one|two|three|four|five|six|seven|eight|nine"
sum = 0
with open("D:\Dipu\Practice\Python\Advant of code\day 1\input.txt", "r") as f:
    for i in f.readlines():
        line = i.strip()
        lists2.append(line)
        digit = ""

        while (re.findall(num_string, line)):
            match = re.findall(num_string, line)
            val = dicts.get(match[0])
            line = line.replace(match[0], val)

        lists.append(line)
               
for i in range(len(lists)):
    digit = [char for char in lists[i] if char.isdigit()]
    sum = sum + int(digit[0]+digit[-1])

print(sum)