#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")
while len(numero) > 4:
    numero = input("El número debe tener hasta 4 dígitos. Ingrese otro número: ")

if len(numero) == 4:
    print(numero[0] + "M + " + numero[1] + "C + " + numero[2] + "D + " + numero[3] + "U")
elif len(numero) == 3:
    print(numero[0] + "C + " + numero[1] + "D + " + numero[2] + "U")
elif len(numero) == 2:
    print(numero[0] + "D + " + numero[1] + "U")
else:
    print(numero[0] + "U")