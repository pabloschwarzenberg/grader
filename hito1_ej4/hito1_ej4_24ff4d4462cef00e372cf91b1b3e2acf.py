n= int(input("Introduzca un número a convertir en binario: "))
def dtobinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario= str(decimal % 2) + binario
        decimal= decimal // 2
    return str(decimal) + binario


print("resultado=",dtobinario(n))