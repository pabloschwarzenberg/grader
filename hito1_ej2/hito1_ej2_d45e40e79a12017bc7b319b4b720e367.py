
from ast import Pass


numero= int(input("ingrese numero de telefono:      "))
hora= eval(input("ingrese hora:    "))

nn=str(numero)
a=nn[-1]
b=nn[-2]
c=nn[-3]
d=a+b+c
e=int(d)
f=nn[0]
g=nn[1]
h=nn[2]
i=f+g+h
j=int(i)

if hora <= 7 and hora >=00:
    mensaje=print("contestar")
elif hora <=14 and e==909:
    print("contestar")
elif hora>=17 and hora<=19 and j !=877:
    print("contestar")
elif hora >19:
    print("no contestar")

elif hora>=17 and hora<=19 and j ==877:
    print("no contestar")
