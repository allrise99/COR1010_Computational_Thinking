a = input("enter scores : ")

alist = a.split(" ")
#[80, 80]
# 0   1
print(alist)
adict = {}
for i in range(0, len(alist)) :
    adict[int(alist[i])] = adict.get(int(adict[i]), 0) + 1
#adict[80] = 1
    


print(adict)
