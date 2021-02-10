list_qu =[]
list_result=[]

aef = input()
ttk = aef.split(' ')
how_many = int(ttk[0])
what = int(ttk[1])

a=1
for i in range(1,how_many+1):
    list_qu.append(i)

while list_qu:
    if a%what==0:
        list_result.append(list_qu[0])
        list_qu.pop(0)
    else:
        list_qu.append(list_qu[0])
        del list_qu[0]

    a+=1
li = list(map(str, list_result))
print('<'+", ".join(li)+'>')