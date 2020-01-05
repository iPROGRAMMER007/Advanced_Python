import re

pattern = ["this","that"]

text = 'this is the passage which contains this only not the other'

if re.search("this",text):
    print("Match Found")
else:
    print("Match not found")







