import random

lista = ["hola", "paralelepipedo", "arroz", "cucamonga", "oruga"]
intentos = 7
palabraS = lista[random.randint(0,4)]


def ocultar_letras(palabra, cantidad):
    contador = cantidad
    palabralista = list(palabra)
    while contador != 0:
        y = random.randint(1, len(palabra) - 1)
        palabralista[y] = "_"
        nuevo = "".join(palabralista)
        contador -= nuevo.count("_")
        if contador != 0:
            contador += nuevo.count("_")
    return nuevo


def revisar_letra(palabra_secreta, palabra, letra):
    lista2 = []
    contador = -1
    for i in palabra_secreta:
        contador += 1
        if i == str(letra):
            lista2.append(contador)
    palabralista = list(palabra)
    for i in lista2:
        print(lista2.index(i))
        palabralista[i] = palabra_secreta[i]
    nuevapalabra = "".join(palabralista)
    return nuevapalabra
