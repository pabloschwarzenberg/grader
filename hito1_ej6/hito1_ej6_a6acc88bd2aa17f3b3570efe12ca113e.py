#Ordenar tres números
l=[]
a=""
for x in range(3):
    n=int(input(":"))
    l.append(n)
    l.sort()
for x in l:
    if not x==l[len(l)-1]:
        a+=str(x)+","
    else:
        a+=str(x)
print(a)