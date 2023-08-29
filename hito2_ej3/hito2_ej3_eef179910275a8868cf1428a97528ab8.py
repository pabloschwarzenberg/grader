string=input()
num=int(input())
todos=[]
dup=[]
for i in range(0,round(len(string)/3)):
    if string[i:(i+num)] in todos:
        dup.append(string[i:(i+num)])
    if len(string[i:(i+num)])==num:
        todos.append(string[i:(i+num)])
unique=set(todos).difference(dup)
unique=list(unique)
if len(unique)==0:
    print("ninguna")
else:
    for i in range(0,len(unique)):
        print(unique[i])