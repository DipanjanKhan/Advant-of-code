import re

with open("D:\Dipu\Practice\Python\Advant of code\day 4\input.txt", "r") as f:
    str = f.readlines()

list1 = []
list2 = []
count = 0
countl = []
for i in str:
    count = 0
    lists = re.split("[:|]", i.replace('\n','').strip(" "))
    list1 = lists[1].strip().split(" ")
    list2 = lists[2].strip().split(" ")
    for l in list1:
        if l in list2:
            count +=1
    countl.append(count)

total = 0
time = 0

for i in countl:
    if i !=0:
        n = 1
        for j in range(1, i):
            n = n * 2
        total += n

print (total)
