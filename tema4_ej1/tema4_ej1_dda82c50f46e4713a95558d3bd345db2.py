
from random import randint
def ocultar_letras(palabra, cant):
    num_rand = randint(0, len(palabra)-1)
    palabra_borrada = palabra
    palabra_borrada = palabra.replace(palabra[num_rand], "_", 1)
    cant_borradas = 1
    while True:
        num_rand = randint(0, len(palabra) - 1)
        if palabra_borrada[num_rand] != "_":
            palabra_borrada = palabra_borrada.replace(palabra[num_rand], "_", 1)
            cant_borradas += 1


        if cant_borradas == cant:
            break
    return palabra_borrada
def revisar_letra(palabra_secreta,palabra,letra):

    for i in palabra_secreta:

        if letra == i:
            cont = palabra_secreta.index(letra)

            reemplazado = palabra[cont]
            reemplazador = palabra_secreta[cont]
            print(cont)
            print(palabra[cont])
            print(palabra_secreta[cont])
            palabra = palabra.replace(reemplazado, reemplazador)


    return palabra

if __name__ == "__main__":
    pass
         