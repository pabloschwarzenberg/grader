  def esvocal(letra):
    letra = letra.upper()
    vocal = 'AEIOU'
    tipo = 0
    if letra in vocal:
        tipo = 1
    return(tipo)

# INGRESO
palabra = input('¿Cuál palabra?: ')
m = len(palabra)
while m>9:
    print(' palabra de hasta 9 letras')
    palabra = input('¿Cuál palabra?: ')
    m = len(palabra)

# PROCEDIMIENTO
m = len(palabra)
palabra = palabra.upper()
cadena  = ''
vocal ='AEIOU'
falla = 0

i = 0
while i<m:
    cadena = cadena + str(i+1)
    i = i + 1

# una letra
j = 0
while (j<m) and falla<5:
    letra = palabra[j]
    cual  = esvocal(letra)
    if cual==1:
        pista = ' es vocal'
    else:
        pista = ' es consonante'
    print(cadena)
    print(str(j+1)+pista + ', fallas:'+str(falla))

    unaletra = input('¿cuál letra?: ')
    unaletra = unaletra.upper()

    if unaletra == letra:
        print(' adivinado..!')
        j = j + 1
        nueva = palabra[0:j]+cadena[j:]
        cadena = nueva
    else:
        print(' fallaste, no es la letra..!')
        falla = falla + 1

if falla>=5:
    print(' Fallaste 5 veces, perdiste..!')
else:
    print(' Felicitaciones, ganaste...!!')
