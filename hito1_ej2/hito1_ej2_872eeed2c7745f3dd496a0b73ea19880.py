#Contestador de celular
a=input("Ingrese número telefónico:")
b=input("Ingrese la hora:")

b=int(b)

c=a[5:8]

c=int(c)

d=a[0:3]

d=int(d)


if b>=0  and b<=7:
    print("CONTESTAR")

elif ((b>7 and b<=14) and c==909):
    print("CONTESTAR")

elif ((b>14 and b<17)):
    print("CONTESTAR")

elif ((b>=17 and b<=19)and d!=877):
    print("CONTESTAR")

elif (b>19 and b<0):
    print("No CONTESTAR")

else:
    print("NO CONTESTAR")    