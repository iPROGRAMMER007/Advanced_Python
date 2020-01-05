import re

pattern = ["this","that"]

text = 'this is the passage which contains this only not the other'

for i in pattern:

    if re.search(i,text):
        print("Match Found")
    else:
        print("Match not found")

match = re.search(pattern[0],text)
print(match)





