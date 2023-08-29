from random import randint


def ocultar_letras(palabra, cantidad):
    palabra_lista = list(palabra)
    oculta = []
    i = 0
    while i < cantidad:
        check = randint(0, len(palabra) - 1)
        if check not in oculta:
            oculta.append(check)
            i += 1
    # print(oculta, palabra, cantidad)
    # oculta = [2,4,10]
    for i in oculta:
        palabra_lista[i] = '_'
    palabra = "".join(palabra_lista)
    return palabra


def revisar_letra(palabra_secreta, palabra, letra):
    if letra in palabra:
        # index = [i for i, l in enumerate(palabra) if l == letra[0]]
        index = palabra.index(letra)
        # print('index', index, letra)
        # for i in index:
        palabra_secreta = palabra_secreta[:index] + letra + palabra_secreta[index + len(letra):]  # print(palabra_secreta)
        return palabra_secreta

    return palabra_secreta


if __name__ == "__main__":
    intentos = 0
    lista_con_palabras_secretas = ['calendario', 'semana', 'segundo', 'pequeño', 'hermoso', 'gracias', 'domingo']
    # lista_con_palabras_secretas = ['lepidoptero']

    palabra_al_azar = lista_con_palabras_secretas[randint(0, len(lista_con_palabras_secretas) - 1)]
    # palabra_al_azar = lista_con_palabras_secretas[0]
    palabra_oculta = ocultar_letras(palabra_al_azar, randint(1, len(palabra_al_azar) - 1))

    while intentos < 7:
        print(palabra_oculta)
        val = input('Ingrese su suposición: ')
        palabra_oculta = revisar_letra(palabra_oculta, palabra_al_azar, val)
        if palabra_oculta == palabra_al_azar:
            print('ganaste')
            break
        intentos += 1

    if intentos >= 7:
        print('perdiste')