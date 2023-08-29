def f(x):
 return list(map(int, str(x)))
x=input("ingrese el numero")
num=f(x)
num=num[::-1]
cont=1
m=[]
for i in num:
    if cont==1:
        l="U"
    if cont==2:
        l="D"
    if cont==3:
        l="C"
    if cont==4:
        l="M"
    y=(str(i)+str(l))
    cont+=1
    m.append(y)
n=len(m)
if n==4:
    print(str(m[3])+"+"+str(m[2])+"+"+str(m[1])+"+"+str(m[0]))
if n==3:
    print(str(m[2])+"+"+str(m[1])+"+"+str(m[0]))
if n==2:
    print(str(m[1])+"+"+str(m[0]))
if n==1:
    print(str(m[0]))