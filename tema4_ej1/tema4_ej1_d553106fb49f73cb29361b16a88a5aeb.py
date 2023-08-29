import random


def ocultar_letras(palabra, cantidad):
    letras = len(palabra)
    if cantidad >= letras:
        return '_'*letras

    posiciones = random.sample( range(letras), cantidad )    
    
    for i in posiciones:
        palabra = palabra[:i] + '_' + palabra[i+1:]
    
    return palabra


def revisar_letra(palabra_secreta, palabra, letra):
    
    if letra in palabra_secreta:        
        for i in range(len(palabra)):
            if palabra[i] == '_':
                if palabra_secreta[i] == letra:
                    palabra = palabra[:i] + letra + palabra[i+1:]
                    
    return palabra


if __name__ == '__main__':
    
    palabras_secretas = [ 'hola', 'cocodrilo', 'auto' ]
    
    
    palabra_secreta = random.choice( palabras_secretas )
    palabra = ocultar_letras(palabra_secreta, 5)
    
    print('Comienza el juego con la palabra:')
    print(palabra)
    
    contador = 0
    while contador < 7:
        
        opcion = input('Adivinar palabra? (S/N) ')
        
        if opcion.lower() == 's':
            
            p = input('Ingresar palabra: ')
            
            if p == palabra_secreta:
                print(p)
                print('Ganaste!')
                break
            else:
                print('Palabra incorrecta')
                contador += 1
                
        elif opcion.lower() == 'n':   
            
            letra = input('Elegir letra: ')
            if letra == '' or len(letra)>1:
                print('Invalido')
                
            else:
                res = revisar_letra(palabra_secreta, palabra, letra)
                if res == palabra:
                    print('No esta la letra')
                    contador += 1
                palabra = res
                print(palabra)
                
            if palabra_secreta == palabra:
                print('Ganaste!')
                break

        else:
            print('Opcion invlida')