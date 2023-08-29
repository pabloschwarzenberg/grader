def convertir(numero):
    r= ""
    while numero > 0:
        residuo = numero%2
        r= r + str(residuo)
        numero=numero//2
    return r[::-1]

b=int(input("ingrese un numero: "))
print(convertir(b))