#Juego adivina mi número
from random import *
def generarnumeroaleatorio(minimo,maximo):
    try:
            if minimo > maximo:
                aux = minimo
                minimo = maximo
                maximo = aux
            return randint(minimo, maximo)
    except TypeError:
        print("ingresa Numero")
        return -1
numero_buscado = generarnumeroaleatorio(1,20)

encontrado = False

while not encontrado:
    numero_usuario = int(input("introduce el Numero Buscado"))

    if numero_usuario > numero_buscado:
        print("El Numero que Busca es Menor: ")
    elif numero_usuario < numero_buscado:
        print("El Numero que Buscas Es Mayor: ")
    else:

            encontrado = True
            print("Adivinaste, mi número era ")      