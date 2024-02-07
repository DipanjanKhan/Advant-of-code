import re

symbol = r"[^\w\s.]"
lists = []

with open("D:\Dipu\Practice\Python\Advant of code\day 3\input.txt", "r") as f:
    for i in f.readlines():
        lists.append(i)

digit = ""
f_index = 0
l_index = 0
num = 0
sum = 0
index = -1
int_pat = r"\b\d+\b"
substring1 = ""
substring2 = ""

for i in lists:
    index += 1
    int_match = re.finditer(int_pat, i)
    
    for j in int_match:
            f_index = j.start()
            digit = j.group()
            digit_len = len(digit)
            l_index = f_index + digit_len-1
            num = int(digit)
            
            # Top left corner
            if f_index == 0 and index == 0:
                if (re.search(symbol,i[l_index+1])):
                    sum += num

                else:
                    substing = lists[index+1][f_index:digit_len+1]
                    if re.search(symbol,substing):
                        sum += num
            
            # Top right corner
            elif index == 0 and l_index == len(i)-1:
                if re.search(symbol,i[f_index-1]):
                    sum += num
                    
                else:
                    substing = lists[index+1][f_index-1:len(i)]
                    if re.search(symbol,substing):
                        sum += num 

            # Bottom left corner
            elif f_index == 0 and index == len(lists)-1:
                if re.search(symbol,i[l_index+1]):
                    sum += num
                    
                else:
                    substing = lists[index-1][f_index:l_index+2]
                    if re.search(symbol,substing):
                        sum += num 

            # Bottom right corner
            elif index == len(lists)-1 and l_index == len(i)-1:
                if re.search(symbol,i[f_index-1]):
                    sum += num
                    
                else:
                    substring1 = lists[index-1][f_index:]
                    if re.search(symbol,substring1):
                        sum += num 
            
            # Top middle
            elif index == 0 and f_index != 0 and l_index != len(i)-1:
                if re.search(symbol,i[f_index-1]) != None or re.search(symbol,i[l_index+1]) != None:
                    sum += num

                else:
                    substing = lists[index+1][f_index-1:l_index+2]
                    if re.search(symbol,substing):
                        sum += num

            # left middle
            elif f_index == 0 and index != 0 and index !=len(lists):
                if re.search(symbol,i[l_index+1]):
                    sum += num

                else:
                    substring1 = lists[index+1][f_index:l_index+2]
                    substring2 = lists[index-1][f_index:l_index+2]
                    if re.search(symbol,substring1) or re.search(symbol,substring2):
                        sum += num 

            # right middle
            elif l_index == len(i)-1 and index != 0 and index != len(lists)-1:
                if re.search(symbol,i[f_index-1]):
                    sum += num

                else:
                    substring1 = lists[index+1][f_index-1:]
                    substring2 = lists[index-1][f_index-1:]
                    if re.search(symbol,substring1) or re.search(symbol,substring2):
                        sum += num 

            # Bottom middle
            elif f_index != 0 and l_index !=len(i)-1 and index == len(lists)-1:
                if re.search(symbol,i[f_index-1]) or re.search(symbol,i[l_index+1]) :
                    sum += num

                else:
                    substing = lists[index-1][f_index-1:l_index+2]
                    if re.search(symbol,substing):
                        sum += num 
            
            # Middle
            elif f_index != 0 and l_index !=len(i)-1 and index != 0 and index !=len(lists)-1:
                if re.search(symbol,i[f_index-1]) or re.search(symbol,i[l_index+1]) :
                    sum += num
                    
                else:
                    substring1 = lists[index+1][f_index-1:l_index+2]
                    substring2 = lists[index-1][f_index-1:l_index+2]
                    if re.search(symbol,substring1) or re.search(symbol,substring2):
                        sum += num 
                    
print(sum)          
