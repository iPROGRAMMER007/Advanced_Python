import re

str = input(str())
count = 0

if (re.match(r'4\d\d\d\S\d\d\d\d\S\d\d\d\d\S\d\d\d\d',str) or re.match(r'5\d\d\d\S\d\d\d\d\S\d\d\d\d\S\d\d\d\d',str)
   or re.match(r'6\d\d\d\S\d\d\d\d\S\d\d\d\d\S\d\d\d\d',str) or re.match(r'4\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d',str)
   or re.match(r'5\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d',str) or re.match(r'6\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d',str)):

    for i in range(0,15):
        if str[i] == str[i+1]:
            count +=1
            if count >=3:
                print("Invalid in for loop")
                break
            elif count < 3:
                print("Valid")
                break


else:
    print("Invalid out")









