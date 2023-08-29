#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    
    return unidades, decenas, centenas, miles

numero = int(input("Ingrese un número de hasta 4 dígitos: "))

descomposicion = descomponer_numero(numero)
print("Descomposición:", descomposicion[3], "M +", descomposicion[2], "C +", descomposicion[1], "D +", descomposicion[0], "U")
