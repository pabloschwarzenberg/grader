#Contestador de celular
numero = input("ingrese el numero de telefono")
hora = int(input("ingrese la hora"))
ultimon= numero[5:8]
ultimon = int(ultimon)
primernumero= numero[0:3]
primernumero = int(primernumero)
if (hora <=7 and hora >=0):
    print("contestar")
elif (hora<14):
    if (ultimon == 909):
        print("contestar")
    else:
        print("no contestar")
if (hora >=17 and hora <=19):
    if (primernumero == 877):
        print("no contestar")
    else:
        print("contestar")
elif hora>19:
    print("no contestar")
