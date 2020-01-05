
dic = {'k1':[1,2,3,4],'k2':(112,33,44),'k3':{'key1':'value1','key2':2},'k4':'String','k5':5}
print(dic)
print(dic['k3'])
print(dic['k3']['key2'])

#dictionary Comprehension

dic2 = {i:i**2 for i in range(10)}

print(dic2)

print(dic2.items())
for x in dic2.items():
    #print(x)
    print(x,end='')

for x in dic2.keys():
    print(x)
for x in dic2.values():
    print(x)


for x,y in dic2.items():
    print(x,y)













