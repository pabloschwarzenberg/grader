#importaciones
import random

#constantes
palabras = ["paralelepipedo", "establo", "antaño", "postreros", "indelebles", "inherente", "asir", "maleable",
            "inconmensurable", "conmensurabilidad", "afable", "veraz"]
palabra = random.choice(palabras)
numeros = [1, 2, 3, 4]
cantidad = random.choice(numeros)
cambio = ["_"]

#proceso

def validacion_largo(palabra, cantidad):
    if len(palabra) < 5 and cantidad < 2 and cantidad > 3:
        cantidad = random.choice(numeros)
    elif cantidad <= 3:
         cantidad = random.choice(numeros)
    return cantidad

def ocultar_letras(palabra, cantidad):
    x = 0
    while x < validacion_largo(palabra, cantidad):
        i = random.randint(0, len(palabra) - 1)
        a = palabra[i]
        escondida = palabra.replace(a, "_", validacion_largo(palabra, cantidad))
        x += 1

    return escondida


def revisar_letra(escondida, palabra, l):
    escondida = ocultar_letras(palabra,cantidad)
    if len(l) == 1:
        for i in palabra:
            if l == palabra[i]:
                escondida[i] = l
        return escondida
    elif len(l) == len(palabra):
        for i in palabra:
            if l[i] == palabra[i]:
                return palabra
            else:
                return escondida

if __name__ == "__main__":
    print(ocultar_letras(palabra, validacion_largo(palabra, cantidad)))
    letra = input("Ingrese la letra: ")
    j = 0
    while j <= 7:
        if revisar_letra(ocultar_letras(palabra,cantidad), palabra, letra) == palabra:
            print(revisar_letra(ocultar_letras(palabra,cantidad)),palabra, letra)
            j = 7
        else:
            print(revisar_letra(ocultar_letras(palabra, cantidad)), palabra, letra)
            j += 1
         