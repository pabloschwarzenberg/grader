# Crea una función, que reciba un texto, y retorne el mismo texto traducido a jerigonzo. 
# El Jerigonzo, es un idioma en que después de cada vocal, se agrega una p, y repite la vocal.
from os import system 

vocales="aeiou"

def jerigonzo(palabra):
    for i in vocales: # asigna las vocales una por una en i
        if i in palabra: # si la vocal esta en la palabra continua
            palabra=(palabra.replace(i,i+"p"+i)) # rempalasa la vocal por (vocal + p + vocal)
            print(palabra) # imprime el cambio
    return palabra # retorna el resultado final al finalizar el ciclo (fin)

if __name__ == "__main__":
    system("cls") # limpia la consola
    palabra=str(input("escriba una palabra: "))
    jerigonzo(palabra) # se llama la funcion
