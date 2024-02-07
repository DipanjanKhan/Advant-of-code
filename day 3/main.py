import re

symbol = re.compile(r"[!@#$%^&*-+/?]")
lists = []

with open("D:\Dipu\Practice\Python\Advant of code\day 3\input1.txt", "r") as f:
    for i in f.readlines():
        lists.append(i)

sum = 0
digit = ""
f_index = 0
l_index = 0
num = 0
index = -1
for i in lists:
    index += 1
    for j in range(0,len(i),1):
        if i[j].isdigit():
            if digit == "":
                f_index = j
            digit = digit + i[j]
            
        if digit != "" and i[j-1].isdigit() and (i[j] == "." or symbol.search(i[j]) or j == len(i)-1):
            digit_len = len(digit)
            l_index = f_index + digit_len-1
            num = int(digit)
            
            
            # Top left corner
            if f_index == 0 and index == 0:
                if (symbol.search(i[l_index+1])):
                    sum += num
                    digit = ""
                    
                else:
                    substing = lists[index+1][f_index:digit_len+1]
                    if symbol.search(substing):
                        sum += num 
                        digit = ""
            
            # Top right corner
            elif index == 0 and l_index == len(i)-1:
                if symbol.search(i[f_index-1]):
                    sum += num
                    digit = ""
                    
                else:
                    substing = lists[index+1][f_index-1:len(i)]
                    if symbol.search(substing):
                        sum += num 
                        digit = ""

            # Bottom left corner
            elif f_index == 0 and index == len(lists)-1:
                if symbol.search(i[l_index+1]):
                    sum += num
                    digit = ""
                    
                else:
                    substing = lists[index-1][f_index:l_index+2]
                    if symbol.search(substing):
                        sum += num 
                        digit = ""

            # Bottom right corner
            elif i == len(lists)-1 and l_index == len(i)-1:
                if symbol.search(i[f_index-1]):
                    sum += num
                    digit = ""
                    
                else:
                    substing1 = lists[index+1][f_index:]
                    if symbol.search(substing1):
                        sum += num 
                        digit = ""
            
            # Top middle
            elif index == 0:
                if symbol.search(i[f_index-1]) or symbol.search(i[l_index+1]):
                    sum += num
                    digit = ""

                else:
                    substing = lists[index+1][f_index-1:l_index+2]
                    if symbol.search(substing):
                        sum += num 
                        digit = ""

            # left middle
            elif f_index == 0 and index != 0 and index !=len(lists):
                if symbol.search(i[l_index+1]):
                    sum += num
                    digit = ""

                else:
                    substing1 = lists[index+1][f_index:l_index+2]
                    substing2 = lists[index-1][f_index:l_index+2]
                    if symbol.search(substing1) or symbol.search(substing2):
                        sum += num 
                        digit = ""

            # right middle
            elif l_index == len(i)-1 and index != 0 and index != len(lists):
                if symbol.search(i[f_index-1]):
                    sum += num
                    digit = ""

                else:
                    substing1 = lists[index+1][f_index-1:]
                    substing2 = lists[index-1][f_index-1:]
                    if symbol.search(substing1) or symbol.search(substing2):
                        sum += num 
                        digit = ""

            # Bottom middle
            elif f_index != 0 and l_index !=len(i)-1 and index == len(lists)-1:
                if symbol.search(i[f_index-1]) or symbol.search(i[l_index+1]) :
                    sum += num
                    digit = ""

                else:
                    substing = lists[index-1][f_index-1:l_index+2]
                    if symbol.search(substing):
                        sum += num 
                        digit = ""
            
            # Middle
            elif f_index != 0 and l_index !=len(i)-1 and index != 0 and index !=len(lists)-1:
                if symbol.search(i[f_index-1]) or symbol.search(i[l_index+1]) :
                    sum += num
                    digit = ""
                    
                else:
                    substing1 = lists[index+1][f_index-1:l_index+2]
                    substing2 = lists[index-1][f_index-1:l_index+2]
                    if symbol.search(substing1) or symbol.search(substing2):
                        sum += num 
                        digit = ""

            digit = ""
                    
print(sum)          

                
