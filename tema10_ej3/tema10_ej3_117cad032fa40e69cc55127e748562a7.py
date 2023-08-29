import random
from random import randint

palabras = ["JUAN", "PERRO", "COLOMBIA", "GUAYABA"]
aleatorio = randint(0,3)
palabra = list(palabras[aleatorio]) #convierte la palabra elegida en lista y es guardada en palabra
numeros = ["1","2","3","4","5","6","7","8","9"]
palabrac= palabras[aleatorio]
repetidas= []
igual = []
adivinanza = []
errores=0
aciertos=0

for x in palabra:
    adivinanza.append("_") #según el número de palabras agrega una "_"
    igual.append("-") #genera en la lista "igual" según el número de palabras que tenga "palabra"

jugar = True

while jugar:

    #bucle del juego

    print(adivinanza, "Errores: " + str(errores), " Intentos restantes: " + str(7-errores))

    jugador = input("Ingrese una letra: ").upper()

    if len(jugador) > 1:
        jugador = input("Ingrese una letra: ").upper() #si hay más de una letra se ejecuta este código

    for z in repetidas:
        if jugador == z:
            jugador = input("Ingrese una letra distinta: ").upper() #busca si la letra está repetida en la lista "repetidas"

    if len(jugador) <1:
        jugador = input("Ingrese una letra: ").upper() #si no se ingresa nada se ejecuta este código

    for n in numeros:
        if jugador == n:
            jugador = input("Ingrese una letra: ").upper() #si hay un número en la entrada se ejecuta


    for x in palabra:

        if jugador == x:
            adivinanza[palabra.index(x)] = jugador

            '''sí la letra está en la lista 'palabras', en la lista "adivinanza" que es la  que se muestra en pantalla
            será cambiada por la letra; para esto tomamos el índice de "x" que es un elemento en lista y lo reemplazamos
            por el índice de "adivinanza", ya que como ambas contienen los mismo elementos, sus índices son los mismos'''

            palabra[palabra.index(x)] = "-"

            '''esto es si la letra está más de una vez, sí no se pone, solo se agregará una vez y se vuelve a escribir
            no se agregará, esto es debido a que el bucle al volverse a ejecutar, encuentra solo la primera y las otras no y
            cada vez que se ejecute seguirá igual, para entenderlo puedes quitar este trozo ese trozo de código y ejecutar
            el programa, repitiendo una letra que hayas escrito'''

            '''Cabe aclarar que también estamos alterando la lista "palabra", ya que el índice de la letra que escribimos
            es reemplazada por el carácter "-"'''

            repetidas.append(jugador)


            if palabra == igual:
                print("Ganaste!")

                '''como se dijo antes "palabra" va a cambiar cada vez que acertemos, por lo que sí acertamos todas palabras
                letras el resultado final de palabra va a ser que todos sus elementos sean "-"'''
                jugar = False

    if jugador not in palabrac:
        errores+=1

        '''palabrac que está al inicio almacena la palabra elegida, pues palabra va a cambiar, si la letra que el
        jugador indica no está en esa lista, la variable errores aumentará 1

        P.D: mirar con cuidado las variables, listas, bucles, etc que hay al principio, para entender que son y
        que contienen, y porqué se usan aquí'''

        if errores == 7:
            print("""\nPérdiste!

La palabra era: """+ palabrac)
            jugar = False

        '''Sí errores es igual a 7, el juego terminará'''


           