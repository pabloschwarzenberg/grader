#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    return unidades, decenas, centenas, miles

numero = int(input("Ingresa un número de hasta 4 dígitos: "))
unidades, decenas, centenas, miles = descomponer_numero(numero)
print(miles,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U")