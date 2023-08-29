b=input()
n=input()
l=[]
cont=0
for k in n:
    l.append(b[cont:].find(k))
    cont=cont+b[cont:].find(k)+1
for i in range(0,len(l)):
    if l[i]==-1:
        l[i]=0
print(l)
nuevo=[]
for cont in n:
    nuevo.append(cont)
print(nuevo)
for i in range(0,len(nuevo)):
    if l[i]!=0:
        esp=""
        for j in range(0,l[i]):
            esp=esp+"_"
        nuevo[i]=esp+nuevo[i]
print("".join(nuevo))