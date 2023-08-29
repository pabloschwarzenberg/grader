import random

palabras = ["lepidoptero", "macrometro", "ubuntu"]

def ocultar_letras(palabra, cantidad):
    contador = 0
    cambio = ""
    for i in palabra:
        aleatoreo = random.randint(0, 1)
        if aleatoreo == 1 and contador != cantidad:

            i = "_"
            contador += 1
        cambio += i
    print(cambio)
    return cambio

def revisar_letra(palabra,palabra_secreta,letra):
    respuesta = ""
    if letra == palabra:
        return palabra
    if letra in palabra:
        for i in range(len(palabra_secreta)):
            if palabra[i] in letra:
                print(i)

                if palabra[i] != palabra_secreta[i]:

                    respuesta = palabra_secreta[:i] + palabra[i] + palabra_secreta[i+1:]
                    print (respuesta)
                    break
                else:
                    print (respuesta)

    return respuesta