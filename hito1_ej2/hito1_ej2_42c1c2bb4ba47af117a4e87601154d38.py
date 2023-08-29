#Contestador      
e = int(input("ingrese numero de telefono: "))
h = int(input("ingrese hora de llamda: "))
r = e % 10
b = int((e % 100) / 10)
p = int((e % 1000) / 100)
y = str(p)+str(b)+str(r)
c6 = int((e % 1000000) / 100000)
c7 = int((e % 10000000) / 1000000)
c8 = int((e - (e % 10000000)) / 10000000)
c10 = str(c8) + str(c7)+str(c6)
if h>=0 and h<=7:
    print("contestar llamada")
elif h>=13 and h<14 :
    print("contestar llamada")
elif h<14:
    print("contestar llamada")
elif h>=8 and h<=12 and y==909:
    print("contestar llamada")
elif h>=17 and h<=19 and c10==877:
    print("contestar llamada")
elif h>=19 and h<=23:
    print("no contestar")
else:
    print("no contestar")