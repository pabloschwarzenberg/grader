numero = int(input("Ingrese telefono: "))
hora = int(input("Ingrese la hora: "))
numero = str(numero)
b = 909
b = str(b)
c = 877
c= str(c)
if (numero[7]):
    if (hora >= 0 and hora <=7):
        print("Contestar")
    elif (hora >= 17 and hora <= 19 and numero[0:3] != c):
        print("Contestar")
    elif (hora >=8 and hora <=14 and numero[5:8]== b):
        print("Contestar")
    elif (hora > 19):
        print("No contestar")
    else:
        print("No contestar")
else:
    print("Otro caso")