#Contestador de celular
n= str(input("Ingrese numero de telefono: "))
h= int(input("Ingrese la hora: "))

u3=n[-3:]
p3=n[0:3]


if((h>=0 and h<=7) or (h<14 and u3=="909") or ((h>=17 and h<=19) and p3!="877")):
    print("Resultado: contestar")
else:
    print("Resultado: no contestar")

