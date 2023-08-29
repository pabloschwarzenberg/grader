import random
def buscarTodas(a,b):
    indices = ''
    i = 0
    while i <= len(a):
        indice = a.find(b,i)
        if indice == -1:
            break
        indices += str(indice) + ' '
        i = indice + 1
    return indices.strip()

lista_de_palabras = ['palabra','papiro','cogote','caracoles','tengo','escondite','hacer','asentamiento']

palabra_secreta = random.choice(lista_de_palabras)

cantidad_ocultas = random.randint(1, len(palabra_secreta) - 1)

def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)
    i = 0
    while i < cantidad:
        indice = random.randint(0, len(palabra) - 1)

        if not palabra[indice] == '_':
            palabra[indice] = '_'
            i += 1

    return ''.join(palabra)

colgadito = ocultar_letras(palabra_secreta, cantidad_ocultas)

def revisar_letra(palabra_secreta,pespacios,letra):
    global colgadito
    pespacios = list(pespacios)

    if palabra_secreta.find(letra) != -1:
        indices = buscarTodas(palabra_secreta, letra)
        indices = indices.split(' ')
        for indice in indices:
            pespacios[int(indice)] = letra
    pespacios = ''.join(pespacios)
    colgadito = pespacios
    return colgadito
    
 
        
    
