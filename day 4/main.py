import re

list1 = []
list2 = []
count = 0
count_list = []

with open("D:\Dipu\Practice\Python\Advant of code\day 4\input.txt", "r") as f:
    
    for i in f.readlines():
        count = 0
        lists = re.split("[:|]", i.strip())
        list1 = re.split(" ", lists[1])
        list2 = re.split(" ", lists[2])

        for l in list1:
            if l in list2 and l != "":
                count += 1
        count_list.append(count)

total = 0
for i in count_list:
    if i != 0:
        n = 2 ** (i-1)
        total = total + n 

print (total)
