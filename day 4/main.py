import re

with open("sample.txt", "r") as f:
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
for i in range(0, len(countl)):
    if countl[0] == countl[i]:
        total = total + (countl[0]*2)
    else:
        total = total + countl[i]
print (total)

    


        