def rot13(palabra):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    palabra_minusculas = palabra.lower()
    for i in range(len(palabra_minusculas)):
        posicion = alfabeto.find(palabra_minusculas[i])
        if posicion <= 12:
            lista_letras = list(palabra_minusculas)
            lista_letras[i] = alfabeto[(int(posicion) + 13)]
            palabra_minusculas = "".join(lista_letras)
        if posicion >= 13:
            lista_letras = list(palabra_minusculas)
            lista_letras[i] = alfabeto[(int(posicion) - 13)]
            palabra_minusculas = "".join(lista_letras)
    return palabra_minusculas


           