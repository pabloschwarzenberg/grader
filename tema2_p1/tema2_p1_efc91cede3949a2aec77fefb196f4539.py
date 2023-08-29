"""
10.- Escribe una función llamada es_primo que retorne True cuando un número
es primo y False cuando no lo es.
"""

def es_primo(numero):
    resultado = True
    for n in range(2, numero):
        if (numero%n) == 0:
            resultado = False
    return resultado

num = int(input("Ingrese un número: "))

if es_primo(num):
    print("El número es primo.")
else:
    print("El número no es primo")