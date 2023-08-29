import random
vida = 7
def ocultar_letras(palabra,cantidad):
    listaPalabra = list(palabra)
    x = 1
    while x <= cantidad:
        y = random.randint(0,len(palabra) - 1)
        while y < len(palabra):
            if listaPalabra[y] != '_':
                listaPalabra[y] = '_'
                x += 1
                break
            else:
                y = random.randint(0, len(palabra) - 1)
    palabraOculta = ''.join(listaPalabra)
    return palabraOculta

def revisar_letra(palabra_secreta,palabra,letra):
    global vida
    palabra = ''
    listaRevisar = list('le_i_opter_')
    if len(letra) == 1:
        z = 0
        x = 0
        while z == 0 and x < len(palabra_secreta):
            if letra == palabra_secreta[x]:
                z = 1
            else:
                x += 1
        if z == 0:
            vida -= 1
        x = 0
        while x < len(listaRevisar):
            if listaRevisar[x] == '_' and palabra_secreta[x] == letra:
                listaRevisar[x] = letra
            x += 1
        nuevaPalabra = ''.join(listaRevisar)
        return nuevaPalabra
    elif len(letra) != 1:
        if palabra_secreta == letra:
            return palabra_secreta
        else:
            vida -= 1


listaPalabras = ['lepidoptero','helicoptero','bicicleta','computador','teclado','lampara','musica','cuaderno','estuche','parlante','perro','luz']
posPalabra = random.randint(0,len(listaPalabras) - 1)
palabraRand = listaPalabras[posPalabra]
letra = ''

if len(palabraRand) <= 3:
    palabraOculta = ocultar_letras(palabraRand,1)
elif 3 < len(palabraRand) <= 5:
    palabraOculta = ocultar_letras(palabraRand, 2)
elif 5 < len(palabraRand) <= 7:
    palabraOculta = ocultar_letras(palabraRand, 3)
elif 7 < len(palabraRand) <= 9:
    palabraOculta = ocultar_letras(palabraRand, 4)
elif 9 < len(palabraRand) <= 11:
    palabraOculta = ocultar_letras(palabraRand, 5)
elif 11 < len(palabraRand):
    palabraOculta = ocultar_letras(palabraRand, 6)
game = 1
while game == 1:
    if palabraOculta != palabraRand:
        palabraOculta = revisar_letra(palabraRand,palabraOculta,letra)
    if vida == 0:
        game = 0
    elif palabraOculta == palabraRand:
        game = 0