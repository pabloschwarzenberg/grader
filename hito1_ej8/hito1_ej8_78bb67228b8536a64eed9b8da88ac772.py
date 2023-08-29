#Descomponer un número
Numero = int(input("Ingrese un número de hasta 4 dígitos: "))
Digitos = list(str(Numero))

Cantidad = len(Digitos)

while (Cantidad > 4):
    print("Debe tener solo 4 dígitos como máximo")
    Numero = int(input("Ingrese un número de hasta 4 dígitos: "))

if (Cantidad == 1):
    Digito1 = Digitos[0] + "U"
    print(str(Digito1))

elif (Cantidad == 2):
    Digito1 = Digitos[1] + "U"
    Digito2 = Digitos[0] + "D"
    print(str(Digito2), "+", str(Digito1))

elif (Cantidad == 3):
    Digito1 = Digitos[2] + "U"
    Digito2 = Digitos[1] + "D"
    Digito3 = Digitos[0] + "C"
    print(str(Digito3), "+",str(Digito2), "+",str(Digito1))

elif (Cantidad == 4):
    Digito1 = Digitos[3] + "U"
    Digito2 = Digitos[2] + "D"
    Digito3 = Digitos[1] + "C"
    Digito4 = Digitos[0] + "M"
    print(str(Digito4), "+",str(Digito3), "+",str(Digito2), "+",str(Digito1))
