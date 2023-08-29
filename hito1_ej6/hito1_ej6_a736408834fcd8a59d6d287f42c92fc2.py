#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
from os import system
system ("cls")

def ordenar(n_1,n_2,n_3):
    lista_numeros=[n_1,n_2,n_3]
    lista_numeros.sort()
    return lista_numeros

n_1 = int(input("Ingrese el primer numero: "))
n_2 = int(input("Ingrese el segundo numero: "))
n_3 = int(input("Ingrese el tercer numero: "))
print(ordenar(n_1,n_2,n_3))
