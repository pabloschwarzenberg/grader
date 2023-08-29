def ocultar_letras(palabra,cantidad):
    import random
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in letras_ocultas:
        palabra_oculta[i] = '_'
    palabra = ' '.join(palabra_oculta)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    nueva_palabra = ''
    if len(letra) == 1:
        if letra in palabra_secreta:
            for i in range(len(palabra)):
                if palabra_secreta[i] == letra:
                    nueva_palabra += letra
                else :
                    nueva_palabra += palabra[i]
            palabra = nueva_palabra
            print('correcto')
        else:
            print('incorrecto')
    else:
        if letra ==  palabra_secreta:
            palabra = palabra_secreta
            print('correcto')
        else:
            print('incorrecto')

    return palabra

if __name__ == "__main__":
    pass
         