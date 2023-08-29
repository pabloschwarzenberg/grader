#Conversión de Decimal a Binario
def decimalabinario(decimal):
    if decimal == 0:
        return "" 
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
#colocar los condicionantes con el caso while para el caso especial de 0 que da 0
    return binario

decimal = int(input("Ingrese un numero decimal: "))
#preguntar el numero decimal que pasaremos a binario

res = decimalabinario(decimal)
#convertir el número decimal a binario

print("Resultado =", res)
#imprimir el resultado