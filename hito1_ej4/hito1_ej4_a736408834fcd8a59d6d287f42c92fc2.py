#Escribe un programa que reciba como entrada un número decimal e imprima el resultado de convertirlo a binario. Por ejemplo, al ingresar el número 33 tu programa debiera imprimir el siguiente mensaje:
#resultado=100001
from os import system
system ("cls")
def decimal_a_binario(numero):
    entero = int(numero)
    decimal = numero - entero
    
    entero_binario = ''
    while entero > 0:
        entero_binario = str(entero % 2) + entero_binario
        entero = entero // 2
    
    decimal_binario = ''
    while decimal > 0 :
        decimal = decimal * 2
        if decimal >= 1:
            decimal_binario += '1'
            decimal -= 1
        else:
            decimal_binario += '0'
    
    if decimal_binario:
        resultado_binario = entero_binario + '.' + decimal_binario
    else:
        resultado_binario = entero_binario
    
    return resultado_binario

numero = float(input("Ingrese un número decimal: "))
resultado_binario = decimal_a_binario(numero)

print("Resultado =", resultado_binario)