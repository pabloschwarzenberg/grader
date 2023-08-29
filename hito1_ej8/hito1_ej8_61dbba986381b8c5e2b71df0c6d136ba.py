#Descomponer un número
#DATOS:

Milésima = print("1000 = 1M")
Centena = print("100 = 1C")
Decena = print("10 = 1D")
Unidad = print("1 = 1U")

#DESARROLLO SISTEMA:

A = int(input("Ingrese un número de hasta 4 digitos:"))
while len(str(A)) > 4 or A < 1:
    A = int(input("Ingrese un número de hasta 4 digitos:"))
XA = str(A)
if len(str(A)) == 4:
    print(XA[0] + "M + " + XA[1] + "C + " + XA[2] + "D + " + XA[3] + "U")
elif len(str(A)) == 3:
    print(XA[0] + "C + " + XA[1] + "D + " + XA[2] + "U")
elif len(str(A)) == 2:
    print(XA[0] + "D + " + XA[1] + "U")
elif len(str(A)) == 1:
    print(XA[0] + "U")
