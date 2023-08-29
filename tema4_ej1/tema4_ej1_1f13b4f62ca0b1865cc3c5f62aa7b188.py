from random import choice, seed, randint

def ocultar_letras(palabra,cantidad):

    largo = len(palabra)
    while palabra.count('_') < cantidad: 

        pos = randint(1,largo) - 1

        if palabra[pos] != '_': 
            palabra = list(palabra)
            palabra[pos] = '_'
            palabra = ''.join(palabra)
        else: 
            continue 

    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):

    palabra_secreta = palabra_secreta.lower()
    letra = letra.lower()
    palabra = list(palabra)
    cant = palabra_secreta.count(letra)
    pos = -1
    for c in range(cant): 
        pos = palabra_secreta.find(letra, pos+1)
        if pos != -1: 
            palabra[pos] = letra
    
    palabra = ''.join(palabra)
    return palabra

if __name__ == "__main__":

    palabras = [
        'esternocleidomastoideo',
        'anticonstitucionalidad',
        'electroencefalografia',
        'contrarrevolucionario',
        'interdisciplinariedad',
        'desoxirribunocleotido',
        'otorrinolaringologia'
    ]

    palabra_secreta = choice(palabras)
    cantidad_oculta = randint(1,len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, cantidad_oculta)

    print('La palabra oculta corresponde a:\n', palabra_oculta, '\n')

    cant_intentos = 0
    while cant_intentos < 7: 

        print('Intente una letra o la palabra completa')

        intento = input('-> ')

        if len(intento) == len(palabra_secreta): 
            print('\nSe ha intentado resolver con la palabra completa')
            if intento.lower() != palabra_secreta.lower(): 
                print(intento.lower() , palabra_secreta.lower() )
                print('Pero respusta es incorrecta')
                cant_intentos += 1
                continue
            else: 
                print('La respuesta es correcta! Felicitaciones')
                break
        
        else: 
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, intento)
            print('\nLa nueva palabra oculta ha quedado en:\n', palabra_oculta, '\n')
            cant_intentos += 1
            
            if palabra_oculta.lower() == palabra_secreta.lower(): 
                print('Felicitaciones! Ha resuelto la palabra')
                break
    
    else: 
        print('\nLos intentos han finalizado. \nLa palabra secreta era: \n', palabra_secreta)
