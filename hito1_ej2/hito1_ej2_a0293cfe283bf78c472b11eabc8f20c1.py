telefono = int(input("Ingrese el numero telefonico: "))
hora = int(input("Ingrese hora de la llama: "))
telefono=str(telefono)
a=telefono[5:8]
e=telefono[0:3]
b=909
b=str(b)
c=877
c=str(c)
if telefono[5:8]==b:
    print("CONTESTAR")
elif telefono[0:3]==c:
    print("NO CONTESTAR")
elif hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora>=8 and hora<14:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
