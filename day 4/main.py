import re

with open("input.txt", "r") as f:
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
for i in range(0, len(countl)):
    if countl[i] == countl[0] and i != 0 and time<=3:
        total = total + (countl[0] * 2)
        time += 1
    else:
        total = total + countl[i]
print (total)

    


        