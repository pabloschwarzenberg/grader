#Descomponer un número
numero = input("Ingrese un numero de 4 digitos: ")

if len(numero) == 4:
    m = numero[0]
    c = numero[1]
    d = numero[2]
    u = numero[3]
    print((m + "M"), "+", (c + "C"), "+", (d + "D"), "+", (u + "U"))
elif len(numero) == 3:
    m = numero[0]
    c = numero[1]
    d = numero[2]
    print((m + "C"), "+", (c + "D"), "+", (d + "U"))
elif len(numero) == 2:
    m = numero[0]
    c = numero[1]
    print((m + "D"), "+", (c + "U"))
elif len(numero) == 1:
    m = numero[0]
    print((m + "U"))
else:
    print("No se acepta")