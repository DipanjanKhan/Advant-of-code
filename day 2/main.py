import re

with open("D:\Dipu\Practice\Python\Advant of code\day 2\input.txt",'r') as f:
    str = f.readlines()

no = 0
count = 0
for i in str:
    no += 1
    st = re.split(r'[:;,]', i)
    flag = True
    for j in st:
        l = [j.replace('\n', '').strip().split(' ')]
        
        if l[0][1]=='blue' and int(l[0][0]) > 14:
            flag = False
            break

        if l[0][1]=='red' and int(l[0][0]) > 12:
            flag = False
            break

        if l[0][1]=='green' and int(l[0][0]) > 13:
            flag = False
            break

    if flag:
        count = count + no

print(count)
