from random import randint
def ocultar_letras(palabra,cantidad):
    i = 0
    ocultado = ''
    while i < len(palabra):
        if i < cantidad:
            letra = palabra[randint(0, len(palabra)-1)]
            x = ocultado
            while x == letra:
                letra = palabra[randint(0, len(palabra) - 1)]
            palabra = palabra.replace(letra, '_', 1)
        i += 1
        ocultado = letra
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    i = 0
    incognita = ''
    while i < len(palabra):
        if palabra_secreta[i] != letra:
            incognita += palabra[i]
        else:
            incognita += letra
        i += 1
    return incognita

if __name__ == "__main__":
    lista_palabras = ['helicoptero', 'agua', 'microbio', 'pajaro', 'naranja', 'manzana', 'platano', 'arquero', 'porteria', 'guardameta']
    palabra_secreta = lista_palabras[randint(0,len(lista_palabras)-1)]
    palabra = ocultar_letras(palabra_secreta, 1)
    print(revisar_letra(palabra_secreta, palabra, 'b'))
    pass