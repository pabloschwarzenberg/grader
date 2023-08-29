"""
6.- Escribe un programa que reciba como entrada un número decimal e imprima el 
resultado de convertirlo a binario. Por ejemplo, al ingresar el número 33 tu programa
debiera imprimir el siguiente mensaje:

resultado=100001
"""

numero = int(input("Escriba un número: "))
numero = "{0:b}".format(numero)
print("resultado="+numero)