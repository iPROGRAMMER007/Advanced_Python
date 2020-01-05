#File

file = open("index")

print(file.read())

file.seek(0)

print(file.read())

file.close()

print("x"*40)

with open('index',mode='r') as f:
    print(f.read())


with open('index',mode='a') as g:
    print(g.write("\n This is new line added by me"))

with open('index',mode='r') as h:
    print(h.read())

with open('new.txt',mode='w') as i:
    i.write("New file created by me.")
print('X'*50)
file = open("new.txt")

print(file.read())

print("x"*50)

file = open("new_new.txt",mode="w")

file.write("Another new file created by me.")

file = open("new_new.txt",mode="r")

print(file.read())


