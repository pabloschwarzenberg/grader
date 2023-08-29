import random
palabra = "hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila"
def ocultar_letras(palabra,cantidad):
    indiceDePalabras = random.randint(0, len(palabra) - 1)
    return palabra[indiceDePalabras]
    
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):

    espaciosVacíos = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
    for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()
    return palabra
         